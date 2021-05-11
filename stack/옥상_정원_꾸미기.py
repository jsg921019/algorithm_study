# https://www.acmicpc.net/problem/6198

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

input()
stack = [float('inf')]
answer = 0
for h in map(int, sys.stdin):
    while stack[-1] <= h:
        stack.pop()
    answer += len(stack) -1
    stack.append(h)

print(answer)