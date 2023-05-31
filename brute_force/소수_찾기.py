# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n%d == 0:
            return False
        d += 1
    return True

def solution(numbers):
    answer = set()
    for k in range(1, len(numbers)+1):
        for n in permutations(numbers, k):
            n = int(''.join(n))
            if is_prime(n):
                answer.add(n)
    return len(answer)