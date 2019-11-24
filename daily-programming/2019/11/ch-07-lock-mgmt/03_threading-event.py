"""
chapter 7.3 threading.Event를 사용한 스레드

그닥 유용치는 않아도 main thread가 sub thread에게 
언제 멈출때를 알게 하는지를 보여줌
"""

import threading
import time

stop = threading.Event()

def background_job():
    while not stop.is_set():
        print("i'm still running")
        stop.wait(0.1)

t = threading.Thread(target=background_job)
t.start()
print("thread started")
time.sleep(1)
stop.set()
t.join()
