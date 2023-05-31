# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    for h in range(1, brown):
        w = (brown -4 - 2*h) //2
        if w*h == yellow:
            return [w+2, h+2]