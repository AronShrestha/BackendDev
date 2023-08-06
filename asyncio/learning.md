Async is a co-routine based concurrency model different than multi-threading which provides elegant constructs to write concurrent python code without the use of multiple thread.
For sub-routine function we will define by def in python but incase of async which makes co-routine can be defined by async.
A coroutine is a special function that can give up control to its caller without losing its state. A coroutine is a consumer and an extension of a generator. One of their big benefits over threads is that they don’t use very much memory to execute. Note that when you call a coroutine function, it doesn’t actually execute. Instead it will return a coroutine object that you can pass to the event loop to have it executed either immediately or later on.

```
import asyncio
import time

# A co-routine
async def add(x: int, y: int):
    print("we adding",x,y)
    sumof = x+y
    time.sleep(3)
    print("Sum is ",sumof)
    return sumof

# An event loop
loop = asyncio.get_event_loop()

# Create a function to schedule co-routines on the event loop
# then print results and stop the loop
async def get_results():
    result1 = await add(3, 4)
    result2 = await add(5, 5)

    print("Result are ",result1, result2) 
    loop.stop()

loop.create_task(get_results())

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()
```
![image](https://github.com/krispcall/aron-onboarding/assets/52240049/3427a57b-17e7-4bfd-8c6e-a1f42d57bd86)

Using asyncio.run
```
import asyncio
import time
# A co-routine
async def add(x: int, y: int):
    print("Adding",x,y)
    sumof = x+y
    await asyncio.sleep(3)
    print("Done for ",x,y)
    return sumof

# Create a function to schedule co-routines on the event loop
# then print results and stop the loop
async def get_results():
    # result1 = await add(3, 4)
    # result2 = await add(5, 5)
    # print(result1, result2) 
    group_res = await asyncio.gather(*(add(i,i+1) for i in range(3)))

    print(group_res) 

asyncio.run(get_results())
```

###Understanding concurrency via asyncio
The event loop executes the scheduled co-routines synchronously. But it achieves concurrency by skipping the blocking period of a co-routine to do work for the next co-routine, just using a single thread.

```
import asyncio

# A fast co-routine
async def add_fast(x, y):
    print("starting fast add")
    await asyncio.sleep(3) # Mimic some network delay
    print("result ready for fast add")
    return x + y

# A slow co-routine
async def add_slow(x, y):
    print("starting slow add")
    await asyncio.sleep(5) # # Mimic some network delay
    print("result ready for slow add")
    return x + y

# Create a function to schedule co-routines
async def get_results():
    # task1 = asyncio.create_task(add_slow(3, 4))
    # task2 = asyncio.create_task(add_fast(5, 5))

    # print(await task1, await task2) 
    group_res = await asyncio.gather(add_slow(3,4),add_fast(5,5))
    print("Result :", group_res)
    

asyncio.run(get_results())
```

As we mentioned earlier, the event loop executes the co-routines synchronously in the way we create tasks as per Line numbers: 19, 20. But, once the loop sees a blocking wait, it executes the other co-routine. The below timeline chart tries to capture this phenomenon.
![image](https://github.com/krispcall/aron-onboarding/assets/52240049/26252618-4ae8-4759-944a-7b3ec02efb74)

For I/O bound operations, this is how asynchronous co-routines can save operation time (improve latency) compared to a sequential program. Instead of eight seconds taken by a sequential program, this concurrent program only needs 5 seconds for both the results to be ready.

**Schedule co-routines dynamically (in one go)**

Until now, we scheduled co-routines manually in the code. What if we have to create co-routines at run-time dynamically. The most important construct to do that is asyncio.gather method.

Let us say we have ’n’ number of inputs, and we need to process them concurrently and get back results; asyncio.gather is the default way to go.

Problem statement: We have few integer tuples to be added individually and returned as a result once the operation is complete.
```
import asyncio

# A co-routine
async def add(x: int, y: int):
    return x + y

# Create a function to schedule co-routines on the event loop
# then print results
async def get_results():
    inputs = [(2,3), (4,5), (5,5), (7,2)]

    # Create a co-routine list
    cors = [add(x,y) for x,y in inputs]
    results = asyncio.gather(*cors)

    print(await results) # Prints [5, 9, 10, 9]

asyncio.run(get_results())
```

**Schedule co-routines dynamically (as items are ready)**

Sometimes, you don’t want a waiter to bring all items at once, and you might want to consume one at a time as they are ready. That can be achieved using asyncio.as_completed method. Instead of collecting all concurrent results in one go, we can now consume the earliest available result from scheduled co-routines.
```
import asyncio

# A co-routine
async def add(x: int, y: int):
    return x + y

# Create a function to schedule co-routines on the event loop
# then print results
async def get_results():
    inputs = [(2,3), (4,5), (5,5), (7,2)]
    # Create a co-routine list
    cors = [add(x,y) for x,y in inputs]

    # Prints results of co-routines as they are ready
    # Beware of Non-deterministic ouput. The order can change based on
    # which co-routine finishes first
    for cor in asyncio.as_completed(cors):
        print(await cor)


asyncio.run(get_results())
```

The asyncio.as_completed method takes a list of co-routines, unlike keyword arguments of asyncio.gather method. The asyncio.as_completed returns iterable co-routines that can be used with the await keyword. You can consume the result right away if you want in a for-loop.

**Schedule co-routines with a time deadline**

Sometimes, one needs to schedule a co-routine but only wait for a certain amount of time and stop execution. That is where asyncio.wait_for method comes in handy.

The asyncio.wait_for method takes a co-routine or task with a timeout and raises an exception if the result is not ready within the timeout period. Let us see an example where we have a co-routine to add numbers that take up to five seconds to execute and prepare the result. If we can’t bear that delay, we can specify our custom threshold as a timeout. We can add a simulated block using asyncio.sleep method, and a random delay using Python’s random package.



```
import asyncio
import random

# A co-routine
async def add(x: int, y: int):
    # function can do work between 1 second to 5 seconds
    await asyncio.sleep(random.randrange(1, 5))
    return x + y

# Create a function to schedule co-routines on the event loop
# then print results
async def get_results():
    result = None
    try:
        # Wait for 3 seconds for co-routine to execute
        # result = await asyncio.wait_for(asyncio.gather(*(add(i,i+1) for i in range(3))), timeout=5)
        result = await asyncio.wait_for(add(3, 4), timeout=2)
    except asyncio.exceptions.TimeoutError:
        result = "fallback payload"

    print(result)

asyncio.run(get_results())
```
If that deadline is exceeded by co-routine while executing, a TimeoutError is raised (this exception is from the asyncio package). By using that, we can make decisions about the result.