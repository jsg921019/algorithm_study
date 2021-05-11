#https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3

from itertools import permutations

def solution(expression):
    
    def calc(eq, priority):
        if priority:
            op = priority[0]
            return str(eval(op.join([calc(eq_, priority[1:]) for eq_ in eq.split(op)])))
        else:
            return str(eval(eq))

    answer = 0

    for priority in permutations('-+*', 2):
        answer = max(answer, abs(int(calc(expression, priority))))

    return answer