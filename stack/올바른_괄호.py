# https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3

def solution(s):
    
    cnt = 0
    
    for bracket in s:
        if bracket == '(':
            cnt += 1
        elif cnt > 0:
            cnt -= 1
        else:
            return False

    return cnt == 0