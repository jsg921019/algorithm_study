# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3#

def solution(people, limit) :
    people.sort()
    answer, lo, hi = 0, 0, len(people) - 1
    while lo <= hi :
        if people[lo] + people[hi] <= limit:
            lo += 1
        hi -= 1
        answer += 1
    return answer