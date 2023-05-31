# https://www.acmicpc.net/problem/15655

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

l = list(map(int, sys.stdin.readline().split()))
l.sort()

def visit(s, path=[]):

    if len(path) == m:
        print(*path)
        return

    for i, num in enumerate(l[s:], s):
        path.append(num)
        visit(i+1)
        path.pop()

visit(0)
