import functools
MAX = 1000
def make_arr(x):
    arr = []
    for _ in range(int(MAX/2)):
        if x>1000:
            continue
        x += x
        arr.append(x)
    return arr

not_prime_list = list(map(
        make_arr ,
        map(lambda i : i, range(2,int((MAX**0.5)+1)))
        ))
not_prime_list1 = list(functools.reduce(lambda x,y:x+y, not_prime_list))
prime_list = list(filter(
    lambda x: x not in not_prime_list1, range(2, MAX+1)
    ))
