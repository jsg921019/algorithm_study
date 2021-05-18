# https://www.acmicpc.net/problem/2504

# solution 1 : using stack

import sys
sys.stdin = open('private/input.txt', 'r')
input = sys.stdin.readline

s = input()

def solution(s):
    d = {']':'[', ')':'('}
    paren_stack = []
    num_stack = [0]
    for c in s:
        if c in d:
            if paren_stack and paren_stack.pop() == d[c]:
                num = num_stack.pop()
                if num:
                    num_stack[-1] += (2 if c == ')' else 3)*num
                else:
                    num_stack[-1] += 2 if c == ')' else 3
            else:
                return 0
        else:
            paren_stack.append(c)
            num_stack.append(0)
    if paren_stack:
        return 0
    else:
        return num_stack[0]

print(solution(s))

# solution 2 : using recursion

import sys
sys.setrecursionlimit(10**9)
def f(s):
  if s=='':
    return 1
  p,q=0,0
  for i in range(len(s)-1):
    if s[i]=='(':
      p+=1
    elif s[i]==')':
      p-=1
    elif s[i]=='[':
      q+=1
    else:
      q-=1
    if p==q==0:
      a=f(s[:i+1])
      b=f(s[i+1:])
      if a and b:
        return a+b
      else:
        return 0
  if s[0]=='(' and s[-1]==')':
    return 2*f(s[1:-1])
  elif s[0]=='[' and s[-1]==']':
    return 3*f(s[1:-1])
  return 0
print(f(input()))