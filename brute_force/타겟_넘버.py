# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

from itertools import product
def solution(numbers, target):
    combs = product(*[(x, -x) for x in numbers])
    sums = [sum(comb) for comb in combs]
    return sums.count(target)