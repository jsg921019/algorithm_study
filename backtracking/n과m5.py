# https://www.acmicpc.net/problem/15654

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
l = sys.stdin.readline().split()
l.sort()

def visit(visting=[0]*n, path=[]):
    if len(path) == m:
        print(*path)
    for i in range(n):
        if visting[i] == 0:
            path.append(l[i])
            visting[i] = 1
            visit()
            path.pop()
            visting[i] = 0

visit()