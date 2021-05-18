# https://www.acmicpc.net/problem/10799

import sys

def solution(arrangement):
    arrangement = arrangement.replace('()', '0')
    temp = 0    # "("의 개수 = 현재 진행중인 막대기 개수
    answer = 0

    for i in arrangement:
        if i == "(": temp += 1
        elif i == "0": answer += temp
        else:
            temp -= 1
            answer += 1
    return answer

x = sys.stdin.readline().rstrip()
print(solution(x))