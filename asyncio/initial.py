import asyncio
import random
import time 

# Async.io creates a coroutine thats execution is different 
# from suboutines that normal function creates



async def count(index):
  print(f"Inside the async program for {index}")
  await asyncio.sleep(1)
  print(f"Completed the asyncio task for {index}")

async def main():
  
  await asyncio.gather(count(1),count(3),count(4),count(5))
  print("main task finish :","asyncio-complete")


async def main2():
  for i in range(4):
    await count(i)
  print("main2 ")

if __name__ == "__main__":
    print("Strating the main program")
    s = time.time()
    asyncio.run(main())
    print("When working async time req : ",time.time()-s)
    s2 = time.time()
    asyncio.run(main2())
    print("When working async time req : ",time.time()-s2)
  
#the benefit of awaiting something, including asyncio.sleep(),
#  is that the surrounding function can temporarily cede 
# control to another function that’s more readily able to
#  do something immediately. In contrast, time.sleep() or 
# any other blocking call is incompatible with asynchronous 
# Python code, because it will stop everything in its tracks 
# for the duration of the sleep time.



  
