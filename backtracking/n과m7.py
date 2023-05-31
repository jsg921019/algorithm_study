# https://www.acmicpc.net/problem/15656

# solution 1
import sys
sys.stdin = open('private/input.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

l = sys.stdin.readline().split()
l.sort(key=lambda x: int(x))

result = []

def visit(seq, r):

    if r == 0:
        result.append(seq[1:])
        return

    for num in l:
        visit(seq + ' ' + num, r-1)

visit('', m)
print('\n'.join(result))

# solution 2
n, m = map(int, input().split())
x = [str(i) for i in sorted(map(int, input().split()))]
x_ = [' '+i for i in x]
for _ in range(m-1):
    x = [i + j for i in x for j in x_]
print('\n'.join(x))