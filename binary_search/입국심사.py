# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    lo, hi = 0, min(times)*n
    answer = hi
    while lo <= hi:
        t = (lo + hi) // 2
        n_possible = sum(t//time for time in times)
        if n_possible > n :
            answer = t
            hi = t - 1
        elif n_possible < n:
            lo = t + 1
        else:
            return t - min(t%time for time in times)
    return answer