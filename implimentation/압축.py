# https://programmers.co.kr/learn/courses/30/lessons/17684?language=python3

def solution(msg):
    
    answer = []
    
    # 1
    d = {chr(i) : i-64 for i in range(65, 91)}

    i = 0
    while i < len(msg):

        # 2
        j = i
        while msg[i:j+1] in d and j < len(msg):
            j += 1
        
        # 3
        answer.append(d[msg[i:j]])
        
        # 4
        d[msg[i:j+1]] = len(d) + 1
        i = j
    
    return answer