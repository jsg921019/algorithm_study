# https://programmers.co.kr/learn/courses/30/lessons/76502?language=python3#

from collections import deque

d = {')':'(', ']':'[', '}':'{', '(':')', '[':']', '{':'}'}

def solution(s):

    answer = 0
    flag = 0
    dq = deque(s)
    stack = []
    
    while dq:
        if flag:
            c = dq.popleft()
            open_set = '{(['
        else:
            c = dq.pop()
            open_set = '}])'
        if c in open_set:
            stack.append(c)
        else:
            if stack and stack[-1] == d[c]:
                stack.pop()
                if not stack:
                    answer += 1
            else:
                answer = 0
                stack.append(c)
                flag = not flag

    return 0 if stack else answer