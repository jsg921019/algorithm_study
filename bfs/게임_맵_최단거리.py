# https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque

def solution(maps):
    
    N, M = len(maps), len(maps[0])
    dq = deque([(0,0,1)])

    while dq:
        i, j, d = dq.popleft()
        if i == N-1 and j == M-1:
            return d
        for i_, j_ in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= i_ < N and 0 <= j_ < M and maps[i_][j_] == 1:
                dq.append((i_, j_, d+1))
                maps[i_][j_] = 0
    return -1