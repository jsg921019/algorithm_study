# table sort
# divide and conquer
# 균등 분할
# 항상 NlogN
# 연결리스트로 더 효율적이게 할 수 있음
# https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/

import random

l = [random.randint(-50,50) for _ in range(100)]
l2 = l.copy()

temp = [0]*len(l)

def partition(l, s, e):
    if s >= e:
        return
    m = (s+e)//2
    partition(l, s, m)
    partition(l, m+1, e)
    merge(l,s,m,e)

def merge(l, s, m, e):
    i, i1, i2 = 0, s, m+1
    while i1 <= m and i2 <= e:
        if l[i2] < l[i1]:
            temp[i] = l[i2]
            i2 += 1
        else:
            temp[i] = l[i1]
            i1 += 1
        i += 1
    for j in range(i1, m+1):
        temp[i] = l[j]
        i += 1
    for j in range(i2, e+1):
        temp[i] = l[j]
        i += 1
    l[s:e+1] = temp[:i]

partition(l, 0, len(l)-1)
print(l)
print(l == sorted(l2))