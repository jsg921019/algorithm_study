# https://www.acmicpc.net/problem/2178

# solution 1 : using deque

import sys
from collections import deque
sys.stdin = open('private/input.txt', 'r')
input = sys.stdin.readline

m, n = map(int, input().split())
board = [ list(line.rstrip()) for line in sys.stdin.readlines()]

def bfs(i, j):

    board[i][j] = 0
    q = deque([(0, 0)])

    while q:
        i, j = q.popleft()
        next_d = board[i][j] + 1
        for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            i_, j_ = i+di, j+dj
            if i_ == m -1 and j_ == n - 1:
                return next_d + 1
            if 0 <= i_ < m and 0 <= j_ < n and board[i_][j_] == '1':
                board[i_][j_] = next_d
                q.append((i_,j_))

print(bfs(0,0))

# solution 2: using list

import sys

m, n = map(int, sys.stdin.readline().split())
board = [ list(line.rstrip()) for line in sys.stdin.readlines()]

def bfs(i, j):
    depth = 1
    nodes = [(0,0)]
    board[i][j] = 0
    while (m-1, n-1) not in nodes:
        depth += 1
        temp = []
        for i, j in nodes:
            for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                i_, j_ = i+di, j+dj
                if 0 <= i_ < m and 0 <= j_ < n and board[i_][j_] == '1':
                    board[i_][j_] = 0
                    temp.append((i_,j_))
        nodes = temp
    print(depth)

bfs(0,0)