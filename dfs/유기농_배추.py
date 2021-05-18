# https://www.acmicpc.net/problem/1012

# solution 1 : iteration

import sys
sys.stdin = open('private/input.txt', 'r')
input = sys.stdin.readline

def sol(m, n, k):
    n_worm = 0
    farm = [[0]*n for _ in range(m)]
    cabbage = [[*map(int, input().split())] for _ in range(k)]

    for i, j in cabbage:
        farm[i][j] = 1

    for c in cabbage:
        i, j = c
        if farm[i][j] == 0:
            continue
        n_worm += 1
        farm[i][j] == 0
        stack = [c]
        while stack:
            i, j = stack.pop()
            for i_, j_ in [(i+1, j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= i_ < m and 0 <= j_ < n and farm[i_][j_] == 1:
                    farm[i_][j_] = 0
                    stack.append([i_,j_])
    return n_worm

for _ in range(int(input())):
    print(sol(*map(int, input().split())))

# solution 2: recursion

import sys
sys.setrecursionlimit(3000)
sys.stdin = open('private/input.txt', 'r')
input = sys.stdin.readline

def sol(m, n, k):

    def recur(i, j):
        farm[i][j] = 0
        for i_, j_ in [(i+1, j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= i_ < m and 0 <= j_ < n and farm[i_][j_] == 1:
                recur(i_, j_)

    n_worm = 0
    farm = [[0]*n for _ in range(m)]
    cabbage = [[*map(int, input().split())] for _ in range(k)]

    for i, j in cabbage:
        farm[i][j] = 1

    for i, j in cabbage:
        if farm[i][j] == 1:
            n_worm += 1
            recur(i,j)

    return n_worm

for _ in range(int(input())):
    print(sol(*map(int, input().split())))