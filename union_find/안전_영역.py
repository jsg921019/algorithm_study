# https://www.acmicpc.net/problem/2468

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
d = defaultdict(list)

for i, row in enumerate(sys.stdin.readlines()):
    for j, v in enumerate(map(int, row.split())):
        d[v].append((i, j))

parents = {}

def get_root(coor):
    p = parents[coor]
    temp = []
    while p != coor:
        temp.append(coor)
        p, coor = parents[p], p
    for c in temp:
        parents[c] = p
    return p

answer = 1
n = 0

for v in sorted(map(int, d), reverse=True)[:-1]:
    for i, j in d[v]:
        connected = set()
        for i_, j_ in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= i_ < N and 0 <= j_ < N and (i_, j_) in parents:
                connected.add(get_root((i_, j_)))
        if len(connected) == 0:
            n += 1
            parents[(i, j)] = (i, j)
        elif len(connected) == 1:
            parents[(i, j)] = connected.pop()
        else:
            root = connected.pop()
            n -= len(connected)
            parents[(i, j)] = root
            for coor in connected:
                parents[coor] = root

    if answer < n:
        answer = n

print(answer)