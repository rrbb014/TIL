# O(1)
__author__ = 'rrbb014'

def solution(X, Y, D):
    # write your code in Python 3.6
    if X == Y :
        return 0

    return (Y-X) // D if (Y-X) % D == 0 else ((Y-X) // D) + 1
