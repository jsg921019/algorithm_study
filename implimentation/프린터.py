# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(priorities, location):
    idx, ans = 0, 0
    for p in sorted(priorities, reverse=True):
        while priorities[idx] != p:
            idx = (idx+1)%len(priorities)
        ans += 1
        if idx == location:
            return ans
        idx = (idx+1)%len(priorities)