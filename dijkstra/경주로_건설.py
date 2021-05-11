# https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3

from heapq import heappop, heappush

directions = {(0,1):0, (1,0):1, (-1, 0):2, (0, -1):3}

def get_next_state(c, i, j, d, board):
    next_state = []
    for d_ in directions:
        i_, j_ = i + d_[0], j + d_[1]
        if 0 <= i_ < len(board) and 0 <= j_ < len(board) and board[i_][j_][directions[d_]]==0:
            if d[0] + d_[0] == d[1] + d_[1] == 0:
                continue
            if d == d_:
                next_state.append((c+100, i_, j_, d_))
            else:
                next_state.append((c+600, i_, j_, d_))
    return next_state

def solution(board):
    
    board = [[[x]*4 for x in row] for row in board]
    hq = [(0,0,0,(0,1)), (0,0,0,(1,0))]
    
    while hq:
        c, i, j, d = heappop(hq)

        if board[i][j][directions[d]]:
            continue

        if i == j == len(board)-1:
            return c

        board[i][j][directions[d]] = 1

        for next_state in get_next_state(c, i, j, d, board):
            heappush(hq, next_state)