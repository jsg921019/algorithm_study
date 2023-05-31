# https://programmers.co.kr/learn/courses/30/lessons/68936

from itertools import product

def solution(arr):
    
    def recursion(size, i, j):

        if size == 0:
            return [0, 1] if arr[i][j] else [1, 0]

        r = [recursion(size//2, i_, j_) for i_, j_ in product([i, i+size], [j, j+size])]

        if all(r[i][1] == 0 for i in range(4)):
            return [1, 0]
        
        if all(r[i][0] == 0 for i in range(4)):
            return [0, 1]
        
        return [sum(r[i][j] for i in range(4)) for j in [0, 1]] 

    return recursion(len(arr)//2, 0, 0)