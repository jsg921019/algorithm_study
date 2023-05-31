# https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3#

from math import gcd

def solution(arr):
    answer = 1
    for n in arr:
        answer = answer*n // gcd(answer, n)
    return answer