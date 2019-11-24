"""
셀러리 Task chain

Task 여러개를 연결하는 방법의 예시.
add의 결과가 multiply 1번쨰 인자로 들어감
"""


import celery

app = celery.Celery('05_celery-chain',
        broker='redis://localhost',
        backend='redis://localhost'
)

@app.task
def add(x, y):
    return x+y

@app.task
def multiply(x, y):
    print('first-args', x)
    return x*y

if __name__ == "__main__":
    chain = celery.chain(add.s(4, 7), multiply.s(10))
    print("Chain %s" % chain)
    result = chain()
    print("Task state: %s" % result.state)
    print("Result: %s" % result.get())
    print("Task state: %s" % result.state)
