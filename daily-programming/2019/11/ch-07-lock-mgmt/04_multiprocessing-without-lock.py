"""
chapter 7.2.1 multiprocessing lock
ex 7.4 잠금을 사용하지않고 병렬로 고양이 그리기

프로세스를 사용해 작업부하 분산할땐 여러개의 프로세스가 
접근할 수 있는 lock이 필요하다.

프로세스 잠금이 필요한 경우는
multiprocessing 으로 프로세스를 생성한 경우.
os.fork나 프로세스 관리자를 통해 독립적으로 실행되는 프로세스를 
생성한 경우.
"""

import multiprocessing
import time

def print_cat():
    # wait for bit and flush result
    time.sleep(0.1)
    print("/\\_/\\")
    print("( 0.0 )")
    print(" > ^ < ")

with multiprocessing.Pool(processes=3) as pool:
    jobs = []
    for _ in range(5):
        jobs.append(pool.apply_async(print_cat))
    for job in jobs:
        job.wait()

# 고양이 그림이 뒤섞이는 이유는 모든 프로세스가 stdout을 공유하면서
# 간섭하기 떄문이다
# 이를 해결하기위해선 고양이가 화면에 완전히 출력될때까지 stdout에
# 잠금을 걸어야한다
