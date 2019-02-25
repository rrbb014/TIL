# https://app.codility.com/demo/results/training7BPUGS-VPD/

# First try is use of list for storing 1 or 0 values But, memory error
# Second try is use of hash set but still memory error
# During watch repeat, i found that least common multiplier is blank spot. 
# So, get LCM -> a*b/gcd(a,b) then just LCM divide by M.
# That's we wanna find. 

def solution(N, M):
    if N==M:
        return 1
    elif N==1 or M ==1:
        return N

    def gcd(N, M):
        if N % M == 0:
            return M
        return gcd(M, N%M)
    
    LCM = (N*M) / gcd(N,M)
    return int(LCM / M)