# https://www.acmicpc.net/problem/2252

# using dfs

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

n_par = [0]*(n+1)
l_ch = [[] for _ in range(n+1)]

answer = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    n_par[b] += 1
    l_ch[a].append(b)

heads = []
for head in range(1, n+1):
    if n_par[head] == 0:
        heads.append(head)

while heads:
    answer.extend(heads)
    heads_ = []
    for head in heads:
        for tail in l_ch[head]:
            n_par[tail] -= 1
            if n_par[tail] == 0:
                heads_.append(tail)
    heads = heads_

print(*answer)

# using heapq

import heapq
import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def topologicalSort():
    n, m = map(int, input().split())
    number = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        number[b] += 1
    que = []
    for i in range(1, n+1):
        if number[i] == 0:
            heapq.heappush(que, i)
    res = []
    for i in range(n):
        tmp = heapq.heappop(que)
        res.append(tmp)
        for p in graph[tmp]:
            number[p] -= 1
            if number[p] == 0:
                heapq.heappush(que, p)
    sys.stdout.write(' '.join(map(str,res)))


if __name__ == '__main__':
    topologicalSort()