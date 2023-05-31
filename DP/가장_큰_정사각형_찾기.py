# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3

# solution 1

def solution(board):
    answer = 0
    for i in range(1, len(board)) :
        for j in range(1, len(board[0])) :
            if board[i][j]:
                board[i][j] += min(board[i-1][j-1],board[i][j-1],board[i-1][j])
                if board[i][j] > answer:
                    answer = board[i][j]

    return answer * answer

# solution 2

def solution(board):

    n_rows = len(board[0])
    size = max(board[0])
    
    for i in range(1, len(board)):
        for j in range(n_rows):
            if board[i][j]:
                board[i][j] += board[i-1][j]
            
        consec = 0
        for tmp in board[i]:
            if tmp > size:
                consec += 1
                if consec > size:
                    size += 1
                    break
            else:
                consec = 0

    return size ** 2