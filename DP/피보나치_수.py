# https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3

def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a+b) % 1234567
    return a