# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    s = '0' + bin(n)[2:]
    idx = s.rfind('01')
    s_next = s[:idx] + '10' + s[:idx+1:-1]
    return int(s_next, 2)
