# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    rows, columns = len(relation), len(relation[0])
    answer = set()
    
    def check_minimality(com, n):
        for m in range(1, n):
            for subcom in combinations(com, m):
                if subcom in answer:
                    return False
        return True
    
    def check_uniqueness(com):
        s = {tuple(relation[i][c] for c in com) for i in range(rows)}
        return True if len(s) == rows else False

    for n in range(1, columns+1):
        for com in combinations(range(columns), n):
            if check_minimality(com, n) and check_uniqueness(com):
                answer.add(com)
    
    return len(answer)