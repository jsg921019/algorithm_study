# stable sort
# time : O(n^2)
# space : O(n)
# too many unefficient moves

import random

l = [random.randint(-50,50) for _ in range(100)]
l2 = l.copy()

for i in range(1, len(l)):
    flag = True
    for j in range(len(l)-i):
        if l[j] > l[j+1]:
            flag = False
            l[j], l[j+1] = l[j+1], l[j]
    if flag:
        break

print(l == sorted(l2))