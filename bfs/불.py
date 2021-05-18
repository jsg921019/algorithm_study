# https://www.acmicpc.net/problem/4179

import sys

m, n = map(int, sys.stdin.readline().split())
board = [list(line.rstrip()) for line in sys.stdin.readlines()]

def find_start(m, n, board):
    jihoon, fire = [], []
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'F':
                fire.append((i,j))
            elif board[i][j] == 'J':
                jihoon.append((i,j))
    return jihoon, fire

def solution(m, n, board):
    depth = 0
    jihoon, fire = find_start(m, n, board)
    while jihoon:
        depth += 1
        tmp_fire = []
        for i, j in fire:
            for i_, j_ in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= i_ < m and 0 <= j_ < n and board[i_][j_] == '.':
                    tmp_fire.append((i_,j_))
                    board[i_][j_] = '#'
        tmp_jihoon = []
        for i, j in jihoon:
            for i_, j_ in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= i_ < m and 0 <= j_ < n:
                    if board[i_][j_] == '.':
                        tmp_jihoon.append((i_,j_))
                        board[i_][j_] = '#'
                else:
                    print(depth)
                    return
        jihoon, fire = tmp_jihoon, tmp_fire
    print('IMPOSSIBLE')

solution(m, n, board)