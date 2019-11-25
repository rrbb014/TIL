"""
chapter 8.3 Use Watcher Callback
ex 8.3 - tooz Watcher 사용하기
"""

import sys
import time

from tooz import coordination

# client id 와 group_id 가 인수로 전달되었는지 확인
if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

# Coordinator 객체 얻음
c = coordination.get_coordinator(
        # 빠른 효과 확인을 위해 timeout을 짧게
        "etcd3://localhost/?timeout=3",
        sys.argv[1].encode()
    )

# connection start
c.start(start_heart=True)

group = sys.argv[2].encode()

# create group
try:
    c.create_group(group).get()
except coordination.GroupAlreadyExist:
    pass

# enter group
c.join_group(group).get()

# 그룹에 참여하거나 나갈때 호출되도록
# print 함수를 등록한다

c.watch_join_group(group, print)
c.watch_leave_group(group, print)

while True:
    c.run_watchers()
    time.sleep(2)

# leave group
c.leave_group(group).get()

# exit
c.stop()
