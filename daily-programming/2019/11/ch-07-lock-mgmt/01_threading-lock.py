"""
chapter 7.1 thread lock
파이썬은 여러개의 스레드가 하나의 리소스에 동시접근하는걸 막기위해
threading.Lock을 제공한다
"""
import threading

stdout_lock = threading.Lock()

def print_something(something):
    with stdout_lock:
        print(something)

t = threading.Thread(target=print_something, args=('hello',))
t.daemon=True
t.start()

print_something("thread started")
print()
print("""가능한 출력결과는
        hello
        thread started  혹은

        thread started
        hello

        뿐이다.""")
