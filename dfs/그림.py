# https://www.acmicpc.net/problem/1926

import sys
sys.stdin = open('private/input.txt', 'r')
input = sys.stdin.readline

m, n = map(int, input().split())
board = [line.split() for line in sys.stdin.readlines()]

def dfs(i, j):

    board[i][j] = 0
    q = [(i, j)]
    fill = 0

    while q:
        fill += 1
        i, j = q.pop()
        for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            i_, j_ = i+di, j+dj
            if 0 <= i_ < m and 0 <= j_ < n and board[i_][j_] == '1':
                board[i_][j_] = 0
                q.append((i_,j_))

    return fill

n_fill = 0
max_fill = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == '1':
            fill = dfs(i, j)
            if fill > max_fill:
                max_fill = fill
            n_fill += 1

print(n_fill)
print(max_fill)