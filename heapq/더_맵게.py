# https://programmers.co.kr/learn/courses/30/lessons/42626

from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a + 2*b)
        answer += 1
    return answer