# https://www.acmicpc.net/problem/9663

import sys
sys.stdin = open('private/input.txt', 'r')

n = int(input())
answer = [0]

def visit(n_queens, rd = set(), ld=set(), r=set(range(n))):

    if n_queens == n:
        answer[0] += 1
        return

    l = list(r) if (n%2 == 1 or n_queens) else range(n//2)
    for i in l:
        if (i+n_queens) not in rd and (i-n_queens) not in ld:
            rd.add(i+n_queens)
            ld.add(i-n_queens)
            r.remove(i)
            visit(n_queens+1)
            rd.remove(i+n_queens)
            ld.remove(i-n_queens)
            r.add(i)

visit(0)
if n%2 == 0:
    answer[0] = 2*answer[0]
print(answer[0])