# fixed moves
# unstable sort

import random

l = [random.randint(-50,50) for _ in range(100)]

for i in range(len(l)-1):
    min_idx = i
    for j in range(i+1,len(l)):
        if l[j] < l[min_idx]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]

print(l == sorted(l))