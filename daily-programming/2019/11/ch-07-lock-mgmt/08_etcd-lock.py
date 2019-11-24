"""
chapter 7.3 distributed lock using etcd
ex 7.8 etcd로 잠금 사용
"""

import etcd3

client = etcd3.client()
lock = client.lock('foobar')
lock.acquire()
try:
    print("do something")
finally:
    lock.release()
