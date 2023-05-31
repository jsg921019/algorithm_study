# https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3

def solution(s):
    s = [int(n) for n in s.split()]
    return str(min(s)) + ' ' + str(max(s))