# https://www.acmicpc.net/problem/1406

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
left = list(input().rstrip())
right = []
input()
for cmd in sys.stdin:
    cmd = cmd.rstrip()
    if cmd == 'L':
        if left:
            right.append(left.pop())
    elif cmd == 'D':
        if right:
            left.append(right.pop())
    elif cmd == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[-1])

print(''.join(left), ''.join(right[::-1]), sep='')