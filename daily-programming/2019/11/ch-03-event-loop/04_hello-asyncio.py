import time
import asyncio

async def hello_world():
    print("hello world")
    time.sleep(3)
    return 42

hello_world_coroutine = hello_world()
print(hello_world_coroutine)

print("이벤트 루프를 선언")
event_loop = asyncio.get_event_loop()
try:
    print("entering event loop")
    result = event_loop.run_until_complete(hello_world_coroutine)
    print(result)
finally:
    event_loop.close()

print("마지막 줄 입니다.")
