""" loop.call_later 사용"""

import asyncio

def hello_world():
    print("hello world")

loop = asyncio.get_event_loop()
loop.call_later(10, hello_world)
loop.run_forever()
