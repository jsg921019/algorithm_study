# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    answer = []
    for d in number:
        while k and answer and answer[-1] < d:
            answer.pop()
            k -= 1
        answer.append(d)
    return ''.join(answer)[:-k] if k else ''.join(answer)