# https://www.acmicpc.net/problem/1697

# solution 1 : iterative

import sys
input = sys.stdin.readline

s, e = map(int, input().split())

def sol(s, e):

    if s >= e:
        return s-e
 
    answer = e-s
    step = 0
    nums = [e]

    while nums:
        step += 1
        temp = []
        for n in nums:
            if n%2:
                if n-1 == s:
                    answer = min(answer, step)
                else:
                    temp.append(n-1)
                    temp.append(n+1)
            else:
                if n//2 < s:
                    s - n//2 + step
                    answer = min(answer, s - n//2 + step, n - s + step - 1)
                elif n//2 == s:
                    answer = min(answer, step)
                else:
                    temp.append(n//2)
        nums = temp

    return answer

print(sol(s, e))

# solution 2 : recursion

def c(n,k):
    if n>=k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return 1+min(c(n,k-1),c(n,k+1))
    else:
        return min(k-n, 1+c(n,k//2))
    
n, k = map(int,input().split())
print(c(n,k))