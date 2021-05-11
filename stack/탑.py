# https://www.acmicpc.net/problem/2493

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

input()

stack = [(float('inf'), 0)]
answer = []

for i, h in enumerate(map(int, input().split()), 1):
    while stack[-1][0] < h:
        stack.pop()
    answer.append(stack[-1][1] if stack else 0)
    stack.append((h,i))

print(*answer)