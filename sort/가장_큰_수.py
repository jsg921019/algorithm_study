# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: 3*x, reverse=True)
    return str(int(''.join(numbers)))