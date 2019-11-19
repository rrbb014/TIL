"""
재시도 기능을 추가한 셀러리 task

Task 실행은 실패할 수 있고, 실패 시에 적절히 다루는 것이 중요하다.
Task는 대개 DB나 API같은 외부 서비스에 의존하기에 
연결 실패가 발생했다면 일시적인 현상 일 수 있다.

이때에는 실패 처리 후에 재시도 하는 것이 좋다.

retry_backoff=True는 exponential backoff를 사용해 재시도처리를 한다.
1초 -> 2 - 4 8 16 처럼 지수적으로 증가하는 대기시간을 가짐.
"""

import celery

app = celery.Celery('04_celery-task-retry',
        broker='redis://localhost',
        backend='redis://localhost'
)

@app.task(
        bind=True,
        retry_backoff=True,
        retry_kwargs={'max_retries': 5}
)
def add(self, x, y):
    try:
        return x+y
    except OverflowError as exc:
        self.retry(exc=exc)

if __name__ == "__main__":
    result = add.delay(4,4)
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)
