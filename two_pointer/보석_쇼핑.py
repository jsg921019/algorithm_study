# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3

from collections import Counter

def solution(gems):

    counter = Counter(gems)
    n_gems = len(counter)
    head, tail = 0, len(gems)-1
    
    while head <= tail < len(gems):
        if len(counter) < n_gems:
            if tail == len(gems) -1:
                return answer
            else:
                gem = gems[head]
                counter[gem] -= 1
                if counter[gem] == 0:
                    del counter[gem]
                head += 1
                tail += 1
                counter[gems[tail]] += 1
        else:
            answer = [head+1, tail+1]
            gem = gems[tail]
            counter[gem] -= 1
            if counter[gem] == 0:
                del counter[gem]
            tail -= 1
    return answer