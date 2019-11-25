"""
chapter 8
ex.8-1 그룹 참가
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
        "etcd3://localhost",
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

# list member
members = c.get_members(group)
print(members.get())

# wait for 5 sec
time.sleep(5)

# leave group
c.leave_group(group).get()

# exit
c.stop()


