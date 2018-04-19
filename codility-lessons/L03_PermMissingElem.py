# L03 - PermMissingElem
# O(N) or O(N*logN)
__author__ = 'rrbb014'

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
        
    ideal_set = set(range(1, len(A)+2))
    result = list(ideal_set.difference(A))[0]
    return result