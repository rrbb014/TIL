"""
Schedule a call to hello_world()
https://docs.python.org/3.5/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.call_soon

콜백을 가능한 빨리 호출하도록 준비하십시오.
제어가 이벤트 루프로 리턴 될 때 call_soon ()이 리턴 된 후 콜백이 호출됩니다.
이 메소드는 FIFO큐로 동작합니다. 콜백은 등록된 순으로 호출됩니다.
각 콜백은 반드시 한번 호출됩니다.
콜백 인자 다음의 위치 인자들은 호출되는 콜백에 넘겨집니다.
키워드를 사용할땐, functools.partial을 활용합시다.
"""

from functools import partial
import asyncio
from IPython import embed

def event_generator(event_loop):
    event_loop.call_soon(partial(print, "i'm generator", flush=True))
    event_loop.stop()

def hello_world(event_loop):
    print("Hello world")
    event_loop.stop()

loop = asyncio.get_event_loop()
loop.set_debug(True)            # optional line

try:
    loop.call_soon(hello_world, loop)
    #     callback ^^^^^^^^^^^

    #loop.call_soon(event_generator, loop)
    # 동작안함. 

    loop.call_soon(partial(print, "HELLO_PARTIAL", flush=True))
    loop.run_forever()
finally:
    loop.close()

print("DONE")

"""
이벤트 루프 선언 후, 아직 루프가 동작하지 않은 상황에서 
28, 34번 함수를 이벤트루프에 등록.
그리고 run_forever로 이벤트루프 실행.
이벤트 루프에서 23번 함수의 loop.stop()을 만나면서,
이벤트 루프는 중단 대기, 현재 스케쥴링된 콜백들을 다 처리하고 끝
"""
