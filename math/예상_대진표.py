# https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3

def solution(n,a,b):
    return len(bin((a-1)^(b-1))) -2