# https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3

def solution(land):
    
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][k] for k in range(4) if k != j])

    return max(land[-1])