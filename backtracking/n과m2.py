# https://www.acmicpc.net/problem/15650

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

def visit(start, remaining, path=[]):

    if remaining == 0:
        print(*path)
        return
    
    for j in range(start, n-remaining + 2):
        path.append(j)
        visit(j+1, remaining-1)
        path.pop()

visit(1, m)