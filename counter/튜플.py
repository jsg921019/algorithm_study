# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

from collections import Counter
import re

def solution(s):
    c = Counter(re.findall('\d+', s))
    return [int(k) for k, v in c.most_common()]