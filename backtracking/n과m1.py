# https://www.acmicpc.net/problem/15649

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

path = []
visiting = [0]*n

def visit(remaining):

    if remaining == 1:
        for i in range(1, n+1):
            if not visiting[i-1]:
                print(*path, i)
        return

    for i in range(1, n+1):
        if not visiting[i-1]:
            path.append(i)
            visiting[i-1] = 1
            visit(remaining-1)
            path.pop()
            visiting[i-1] = 0

visit(m)