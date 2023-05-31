# unstable sort
# divide and conquer
# 비균등 분할
# 정렬되어 있을때 최악
#https://gyoogle.dev/blog/algorithm/Quick%20Sort.html

import random

l = [random.randint(-50,50) for _ in range(100)]
l2 = l.copy()

def partition(l, s, e):
    pivot = l[e]
    cursor = s
    for i in range(s, e):
        if l[i] < pivot:
            l[i], l[cursor] = l[cursor], l[i]
            cursor += 1
    l[e], l[cursor] = l[cursor], l[e]
    return cursor

def quick_sort(l, s, e):
    if s >= e:
        return
    pivot = partition(l, s, e)
    quick_sort(l,s,pivot-1)
    quick_sort(l,pivot+1,e)

quick_sort(l, 0, len(l)-1)

print(l == sorted(l2))