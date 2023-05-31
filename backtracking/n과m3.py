# https://www.acmicpc.net/problem/15651

import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

def product(remaining, seq=[]):
    if remaining == 0:
        print(*seq)
        return
    for i in range(1, n+1):
        seq.append(i)
        product(remaining-1)
        seq.pop()

product(m)
