# https://programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict
from bisect import bisect_left
from itertools import product

def solution(info, query):

    info = [info_.split() for info_ in info]
    info.sort(key=lambda x: int(x[-1]))

    d = defaultdict(list)
    for lan, job, career, food, score in info:
        score = int(score)
        for c in product([lan, '-'], [job, '-'], [career, '-'], [food, '-']):
            d[c].append(score)

    answer = []
    for q in query:
        q = q.split()
        field = (q[0], q[2], q[4], q[6])
        answer.append(len(d[field])-bisect_left(d[field], int(q[-1])))

    return answer