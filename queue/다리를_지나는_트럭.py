# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    dq = deque()
    tot_weight = 0
    last_t = 0
    recent_t = 0

    for tw in truck_weights:
        tot_weight += tw
        while tot_weight > weight:
            w, last_t = dq.popleft()
            tot_weight -= w
        recent_t = max(last_t + bridge_length, recent_t + 1)
        dq.append((tw, recent_t))

    return dq[-1][1] + 1