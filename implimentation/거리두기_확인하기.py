# https://programmers.co.kr/learn/courses/30/lessons/81302

def solution_(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                # 1 거리
                for i_, j_ in [(i+1, j),(i, j+1)]:
                    if 0 <= i_ < 5 and 0 <= j_ < 5 and place[i_][j_] == 'P':
                        return 0
                # 2 거리
                for i_, j_ in [(i+2, j),(i, j+2)]:
                    if 0 <= i_ < 5 and 0 <= j_ < 5 and place[i_][j_] == 'P'\
                    and place[(i+i_)//2][(j+j_)//2] != 'X':
                        return 0
                # 대각선
                for i_, j_ in [(i+1, j-1),(i+1, j+1)]:
                    if 0 <= i_ < 5 and 0 <= j_ < 5 and place[i_][j_] == 'P'\
                    and (place[i][j_] != 'X' or place[i_][j] != 'X'):
                        return 0 
    return 1

def solution(places):
    return [solution_(place) for place in places]