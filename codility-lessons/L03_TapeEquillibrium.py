# Codility lessons for programmers 
# L03-Time Complexity - TapeEquillibrium 
# O(N)
__author__ = 'rrbb014'

def solution(A):
    # write your code in Python 3.6
    first_val = 0
    second_val = sum(A)
    min_diff = None
    
    for i in range(len(A)-1):
        first_val += A[i]
        second_val -= A[i]
        
        if min_diff == None:
            min_diff = abs(first_val - second_val)
        else:
            min_diff = min(min_diff, abs(first_val - second_val))
    return min_diff