# https://www.acmicpc.net/problem/14567

# 그냥 bfs같은데??

# solution 1
import sys
sys.stdin = open('private/input.txt', 'r')

from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

n_pre = [0]*n
l_pre = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    n_pre[b-1] += 1
    l_pre[a-1].append(b-1)

zeros = [i for i, k in enumerate(n_pre) if k == 0]

semester = 1
answer = [0]*n

while zeros:
    zeros_ = []
    for i in zeros:
        answer[i] = semester
        for b in l_pre[i]:
            n_pre[b] -= 1
            if n_pre[b] == 0:
                zeros_.append(b)
    semester += 1
    zeros = zeros_

print(*answer)


# solution 2
import sys
from collections import deque

def solution():
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    degree = [0] * (N+1)
    time = [0] * (N+1)
    dq = deque()

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        degree[B] += 1

    for i in range(1, N + 1):
        if degree[i] == 0:
            dq.append((i, 1))

    while dq:
        idx, t = dq.popleft()
        time[idx] = t
        for j in graph[idx]:
            degree[j] -= 1

            if degree[j] == 0:
                dq.append((j, t+1))

    for t in range(1, len(time)):
        print(time[t], end=' ')

solution()