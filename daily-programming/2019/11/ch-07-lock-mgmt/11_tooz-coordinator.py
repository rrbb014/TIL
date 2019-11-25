"""
chapter 7.4 lock abstraction with tooz
ex. 7.11 - tooz coordinator

tooz 라이브러리는 서로 다른 잠금 백엔드 분산기능의 추상화를 위해 개발됨.
어떤 서비스에서 다른 서비스로의 전환을 쉽게 가능하게 한다.

이를 위해 Coordination 객체를 통해 app에 연결할 코디네이터 서비스를 제공한다.
"""

import uuid

from tooz import coordination

# UUID를 사용해 고유 식별자 생성
identifier = str(uuid.uuid4())

# Coordination object
c = coordination.get_coordinator(
        "etcd3://localhost",
        identifier
    )

# Coordinator start(connection start)
c.start(start_heart=True)

# When program end, Coordinator also exit
c.stop()
