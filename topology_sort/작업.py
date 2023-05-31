# https://www.acmicpc.net/problem/2056

미완

import sys
sys.stdin = open('private/input.txt', 'r')

n = int(sys.stdin.readline())

n_par = [0]*(n+1)
l_ch = [[] for _ in range(n+1)]
t = [0]

answer = 0

for i in range(1, n+1):
    a, b, *c = map(int, sys.stdin.readline().split())
    t.append(a)
    n_par[i] = b
    for j in c:
        l_ch[j].append(i)

heads = []
for head in range(1, n+1):
    if n_par[head] == 0:
        heads.append(head)

while heads:
    answer += max([t[i] for i in heads])
    heads_ = []
    for head in heads:
        for tail in l_ch[head]:
            n_par[tail] -= 1
            if n_par[tail] == 0:
                heads_.append(tail)
    heads = heads_

print(answer)