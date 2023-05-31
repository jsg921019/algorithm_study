# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = []
    for a, b in zip(' ' + s[:-1], s):
        answer.append(b.upper() if a == ' ' else b.lower())
    return ''.join(answer)