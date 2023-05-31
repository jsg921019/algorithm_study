# https://programmers.co.kr/learn/courses/30/lessons/60057

from itertools import groupby

def solution(s):
    answer = len(s)
    n = 1
    while n < answer:
        length = 0
        chunks = [s[i:i+n] for i in range(0,len(s), n)]
        for a, b in groupby(chunks):
            number = len(list(b))
            if  number == 1:
                length += len(a)
            else:
                length += len(a)+ len(str(number))
        if length < answer: answer = length
        n += 1
    return answer