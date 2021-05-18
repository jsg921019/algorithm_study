# https://www.acmicpc.net/problem/7576

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, line.split())) for line in sys.stdin.readlines()]

cnt = 0
depth = -1
tomatoes = []

for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            cnt += 1
        elif board[i][j] == 1:
            tomatoes.append((i,j))

while tomatoes:
    cnt += len(tomatoes)
    depth += 1
    temp = []
    for i, j in tomatoes:
        for i_, j_ in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0<=i_<n and 0<=j_<m and board[i_][j_] == 0:
                board[i_][j_] = 1
                temp.append((i_,j_))
    tomatoes = temp

print(depth if cnt == m*n else -1)