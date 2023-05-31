# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):

    board = [list(c[::-1]) for c in zip(*board)]

    while 1:
        delete = set()
        for i in range(n-1):
            for j in range(min(len(board[i]), len(board[i+1]))-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    delete.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})
        if delete:
            for i, j in sorted(delete, reverse=True):
                board[i].pop(j)
        else:
            return sum(m - len(c) for c in board)