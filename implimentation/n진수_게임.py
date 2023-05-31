# https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3

num2str = '0123456789ABCDEF'

def solution(n, t, m, p):

    p -= 1
    answer = []
    num = [0]

    while len(answer) < t:

        answer += num[~p::-m]
        p = (p - len(num)) % m

        for i in range(len(num)):
            if num[i] + 1 == n:
                num[i] = 0
            else:
                num[i] += 1
                break
        else:
            num.append(1)

    return ''.join([num2str[x] for x in answer[:t]])