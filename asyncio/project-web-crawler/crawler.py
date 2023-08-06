import pathlib
import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse
import aiofiles
import aiohttp
from aiohttp import ClientSession
import os


WRITE_ONE =0

class CrawlerPathSetup: #pep8 standard for class name 

    def __init__(self, read_file_path, write_file_path) -> None:
        self.parent = pathlib.Path(__file__).parent   # to get current parent directory
        self.read_file_path = os.path.join(self.parent, read_file_path)
        self.write_file_path = os.path.join(self.parent, write_file_path)
    
    def __repr__(self) -> str:
        return f"I read from {self.read_file_path} and write into {self.write_file_path}"

    
class CrawlerFunction:
    def __init__(self) -> None:
        logging.basicConfig(
            format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
            level=logging.DEBUG,
            datefmt="%H:%M:%S",
            stream=sys.stderr,
        )
        self.logger = logging.getLogger("areq")
        logging.getLogger("chardet.charsetprober").disabled = True
        self.HREF_RE = re.compile(r'href="(.*?)"')


    async def fetch_html(self, url:str, session:ClientSession, **kwargs):
        print("In fetch ")
        resp = await session.request(method="GET", url=url, **kwargs)
        resp.raise_for_status()
        self.logger.info("Got response [%s] for URL: %s", resp.status, url)
        html = await resp.text()
        return html
        

    async def parse(self,url: str, session : ClientSession, **kwargs)->set:
        print("In parse ")
        found = set()
        try:
            html = await self.fetch_html(url=url, session=session, **kwargs)

        except (
            aiohttp.ClientError,
            aiohttp.http_exceptions.HttpProcessingError,
        ) as e:
            self.logger.error(
                "aiohttp exception for %s [%s]: %s",
                url,
                getattr(e, "status", None),
                getattr(e, "message", None),
            )
            return found
        except Exception as e:
            self.logger.exception(
                "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
            )
            return found
        else:
            for link in self.HREF_RE.findall(html):
                try:
                    abslink = urllib.parse.urljoin(url, link)
                except (urllib.error.URLError, ValueError):
                    self.logger.exception("Error parsing URL: %s", link)
                    pass
                else:
                    found.add(abslink)
            self.logger.info("Found %d links for %s", len(found), url)
            return found


    async def write_one(self,file, url, **kwargs)->None:
        '''Writing the found HREFs from "url" to file. '''
        global WRITE_ONE
        res = await self.parse(url=url, **kwargs)
        WRITE_ONE += 1
        print("IN write_one", WRITE_ONE)
        if  not res:
            return None
        async with aiofiles.open(file, "a") as f:
            for p in res:
                await f.write(f"{url}\t{p}\n")
            self.logger.info("Wrote results for source URL: %s", url)


    async def crawl_and_write(self, paths: CrawlerPathSetup, **kwargs) -> None:
        async with ClientSession() as session:
            tasks = []  #for gather async task for all the urls in the read_file_path
            with open(paths.read_file_path) as f:
                urls = set(map(str.strip, f))
            print("In crawl")
            for url in urls:
                tasks.append(
                    self.write_one(
                        file=paths.write_file_path, url=url, session=session, **kwargs
                    )
                )
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    crw = CrawlerPathSetup(read_file_path="urls.txt", write_file_path="found_url.txt")
    crf = CrawlerFunction()
    asyncio.run(crf.crawl_and_write(crw))