"""
chapter 7
ex 7.12 - 코디네이터에서 잠금 얻기
"""

import uuid

from tooz import coordination

# UUID를 사용해 고유 식별자 생성
identifier = str(uuid.uuid4())

# coordinator
c = coordination.get_coordinator(
        'etcd3://localhost',
        identifier
    )

c.start(start_heart=True)

lock = c.get_lock(b'name_of_the_lock')

# lock acquire and release
print("lock acquire try")
assert lock.acquire() is True
print("lock release try")
assert lock.release() is True

# 획득하지않은 잠금은 해제못함
print("non-acquired lock release try")
assert lock.release() is False

assert lock.acquire() is True
# 블록하지않고 잠금 획득 시도(실패해도 바로 알수있음)
print("non-blocking lock acquire try")
assert lock.acquire(blocking=False) is False

# 잠금 획득까지 5초간 대기
print("lock acquire wait for 5sec try")
assert lock.acquire(blocking=5) is False
assert lock.release() is True

# 프로그램이 끝나면 coordinator도 종료
print("stop coordinator")
c.stop()
