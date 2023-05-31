# stable sort
# time : O(n^2)
# 최선의 경우 O(n)
# space : O(n)

import random

l = [random.randint(-50,50) for _ in range(100)]
l2 = l.copy()

for i in range(1, len(l)):
    n = l[i]
    j = i-1
    while j >= 0 and l[j] > n:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = n

print(l == sorted(l2))