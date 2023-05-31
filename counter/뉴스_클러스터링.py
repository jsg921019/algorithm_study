# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def to_token(s):
    s = s.lower()
    tokens = [s[i:i+2] for i in range(len(s)-1) if s[i:i+2].isalpha()]
    return Counter(tokens)

def solution(str1, str2):
    c1, c2 = to_token(str1), to_token(str2)
    union, diff = sum((c1 | c2).values()), sum((c1 & c2).values())
    if union:
        return int(sum((c1 & c2).values()) * 65536 / sum((c1 | c2).values()))
    else:
        return 65536