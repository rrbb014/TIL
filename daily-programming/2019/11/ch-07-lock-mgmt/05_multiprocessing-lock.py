"""
chapter 7.2.1 multiprocessing lock
ex 7.5 잠금을 사용해 병렬로 고양이 그리기

"""

import multiprocessing
import time

stdout_lock = multiprocessing.Lock()

def print_cat():
    # wait for bit and flush result
    time.sleep(0.1)
    with stdout_lock:
        print(" /\\_/\\")
        print("( 0.0 )")
        print(" > ^ < ")

with multiprocessing.Pool(processes=3) as pool:
    jobs = []
    for _ in range(5):
        jobs.append(pool.apply_async(print_cat))
    for job in jobs:
        job.wait()

"""
잠금을 사용했기 떄문에 프로세스가 고양이 그림을 그리려면 Lock을 먼저 얻어야한다.
다시 해제하기전에는 다른 프로세스가 그림을 그릴 수 없다.
"""
