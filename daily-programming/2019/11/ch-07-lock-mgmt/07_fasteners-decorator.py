"""
chapter 7
ex 7.7 패스너스 데코레이터 사용하기
"""

import time

import fasteners

@fasteners.interprocess_locked('/tmp/tmp_lock_file')
def locked_print():
    for i in range(10):
        print("I have the lock")
        time.sleep(0.1)

locked_print()

"""
single point of failure(단일 장애점)이 없으므로 local process 사이의 잠금 처리에
좋은 방법이다
"""
