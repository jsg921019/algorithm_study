# https://www.acmicpc.net/problem/12015

import sys
input = sys.stdin.readline

def solution(N, arr):

    def rec(i, prev):
        
        while arr[i] > arr[prev]:
            
        

    return rec(0, -float('inf'))

N = int(input())
arr = [*map(int, input().split())]
print(solution(N, arr))