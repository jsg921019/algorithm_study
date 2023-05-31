# https://www.acmicpc.net/problem/15652

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

def bt(remaining, start, seq=[]):

    if remaining == 0:
        print(*seq)
        return
    
    for i in range(start, n+1):
        seq.append(i)
        bt(remaining-1, i)
        seq.pop()
    
bt(m, 1)