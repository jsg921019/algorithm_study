# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = list(range(len(prices))[::-1])
    stack = []
    for i, n in enumerate(prices):
        while stack and stack[-1][-1] > n:
            j, _ = stack.pop()
            answer[j] = i - j
        stack.append((i, n))
    return answer