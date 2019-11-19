from concurrent import futures
import random

def compute():
    return sum([random.randint(1, 100) for _ in range(1000000)])

with futures.ProcessPoolExecutor(max_workers=4) as executor:
    fut = [executor.submit(compute) for _ in range(15)]

results = [f.result() for f in fut]

print(results)
