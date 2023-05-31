# https://programmers.co.kr/learn/courses/30/lessons/70129?language=python3

def solution(s):
    cnt, rnd = 0, 0
    while s != '1':
        zeros = s.count('0')
        cnt += zeros
        rnd += 1
        s = bin(len(s)-zeros)[2:]
    return [rnd, cnt]