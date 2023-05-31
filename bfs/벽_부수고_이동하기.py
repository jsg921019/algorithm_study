# https://www.acmicpc.net/problem/2206

import sys

def sol(N, M, board):
    if N == 1 and M == 1:
        return 1
    curr_depth = [(0,0,0)]
    cnt = 1
    while curr_depth:
        cnt += 1
        next_depth = []
        for i, j, flag in curr_depth:
            for i_, j_ in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= i_ < N and 0 <= j_ < M:
                    if i_ == N-1 and j_ == M-1:
                        return cnt
                    if flag == 0:
                        if board[i_][j_] == '1':
                            board[i_][j_] = '3'
                            next_depth.append((i_, j_, 1))
                        if board[i_][j_] == '0' or board[i_][j_] == '2':
                            board[i_][j_] = '3'
                            next_depth.append((i_, j_, 0))
                    elif flag == 1 and board[i_][j_] == '0':
                        board[i_][j_] = '2'
                        next_depth.append((i_, j_, 1))
        curr_depth = next_depth
    return -1

N, M = map(int, sys.stdin.readline().split())
board = [list(line.strip()) for line in sys.stdin.readlines()]

print(sol(N, M, board))