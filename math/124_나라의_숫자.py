# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    d = ['1', '2', '4']
    answer = ''
    while n :
        n, r = divmod(n-1, 3)
        answer = d[r] + answer
    return answer