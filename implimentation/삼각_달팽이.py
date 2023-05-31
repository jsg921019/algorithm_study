# https://programmers.co.kr/learn/courses/30/lessons/68645#

from itertools import chain

def solution(n):
    
    answer = [[0]*i for i in range(1, n+1)]
    di = [1, 0, -1]
    dj = [0, 1, -1]
    i, j, m = -1, 0, 0
    for n_ in range(n):
        for _ in range(n - n_):
            m += 1
            i += di[n_ % 3]
            j += dj[n_ % 3]
            answer[i][j] = m
        
    return list(chain.from_iterable(answer))