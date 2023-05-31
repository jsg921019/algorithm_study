# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    return [[sum(i*j for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1]