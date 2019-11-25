"""
chapter 8
ex. 8.2 - tooz capability 사용
"""

import sys
import time

from tooz import coordination

# client id 와 group_id 가 인수로 전달되었는지 확인
if len(sys.argv) != 4:
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
c.join_group(
        group,
        capabilities={"mood": sys.argv[3]}
    ).get()

# list member and capabilities
# API가 비동기 방식이므로 역량을 얻기위한 요청을 동시에 보내서 병렬로 실행되도록 한다
get_capabilities = [
        (member, c.get_member_capabilities(group, member))
        for member in c.get_members(group).get()
    ]

for member, cap in get_capabilities:
    print("Member %s has capabilities: %s" % (member, cap.get()))

# wait for 5 sec
time.sleep(5)

# leave group
c.leave_group(group).get()

# exit
c.stop()
