# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    return [((n ^ (n + 1)) >> 2) + n + 1 for n in numbers]