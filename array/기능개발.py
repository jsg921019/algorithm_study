# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    
    answer = []
    days = [-((p-100)//s) for p,s in zip(progresses, speeds)]
    max_day = 0
    for d in days:
        if d > max_day:
            answer.append(1)
            max_day = d
        else:
            answer[-1] +=1
    return answer