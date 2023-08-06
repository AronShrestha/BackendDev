import asyncio
import os


async def makeitem(size: int = 5) -> str:
    print("Called")
    await asyncio.sleep(3)
    return os.urandom(size).hex()
    

async def main():
    print("Entry")
    # a=await makeitem()
    a = await asyncio.gather(*(makeitem(i) for i in range(3)))
    print(*(i for i in range(3)))#unpacking
    print((i for i in range(3)))
    print("After")
    
    print(a)

asyncio.run(main())