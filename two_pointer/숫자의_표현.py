# https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3

def solution(n):
    
    answer = 0
    head, tail, tot = 1, 1, 0 # head 이상 tail 미만

    while tail <= n + 1:
        if tot < n:
            tot += tail
            tail += 1
        else:
            if tot == n:
                answer += 1
            tot -= head
            head += 1

    return answer