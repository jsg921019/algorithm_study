# https://www.acmicpc.net/problem/9466

import sys
sys.stdin = open('private/input.txt', 'r')
input = sys.stdin.readline

def sol(n, l):

    n_child = [0]*(n+1)

    for i in l:
        n_child[i] += 1
    
    leaf = [i for i in range(1,n+1) if n_child[i] == 0]
    for i in leaf:
        j = l[i-1]
        n_child[j] -= 1
        if n_child[j] == 0:
            leaf.append(j)
    
    return len(leaf)

for _ in range(int(input())):
    print(sol(int(input()), [*map(int, input().split())]))