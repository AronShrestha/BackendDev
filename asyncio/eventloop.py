#You can think of an event loop as something like a while True loop that monitors coroutines, 
#taking feedback on what’s idle, and looking around for things that can be executed in the meantime. 
#It is able to wake up an idle coroutine when whatever that coroutine is waiting on becomes available

#asyncio.run(), introduced in Python 3.7, is responsible 
#for getting the event loop, running tasks until they are 
#marked as complete, and then closing the event loop.
#There’s a more long-winded way of managing the asyncio 
#event loop, with get_event_loop(). The typical pattern 
#looks like this:
#loop = asyncio.get_event_loop()
#try:
#     loop.run_until_complete(main())
#finally:
#     loop.close()
# You’ll probably see loop.get_event_loop() 
# floating around in older examples, but unless 
# you have a specific need to fine-tune control 
# over the event loop management, asyncio.run() should be 
# sufficient for most programs.