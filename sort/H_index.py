# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c <= i:
            return i
    return len(citations)