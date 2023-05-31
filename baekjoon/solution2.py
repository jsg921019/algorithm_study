# https://www.acmicpc.net/problem/14942

import sys
from collections import defaultdict

I = sys.stdin.readline

N = int(I())

energy = [0] + [int(I()) for _ in range(N)]
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, d = map(int, I().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

answer = [0]*(N+1)
prev = [0]*(N+1)
stack = [(1, 0)]

while stack:
    room, d = stack.pop()
    for next_room, cost in graph[room]:
        if not prev:
            prev[next_room] = [room, ]
