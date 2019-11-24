"""
chapter 7
ex 7.6 fasteners를 사용한 인터프로세스 lock

multiprocessing.Lock은 단일 파이썬 프로세스에서 시작된 프로세스에서만 동작한다.
독립적으로 시작된 데몬처럼 애플리케이션이 여러 파이썬 프로세스에 분산되면
프로세스 사이의 lock mechanism이 필요하다.

fasteners가 구현한 잠금은 File system 잠금을 기반으로 한다. 파일시스템 잠금은

파이썬에만 한정된 것이 아니므로 다른 언어로도 동일한 잠금 메커니즘으로 구현가능하다.
"""

import time

import fasteners

lock = fasteners.InterProcessLock("/tmp/mylock")
with lock:
    print("Access Locked")
    time.sleep(1)
