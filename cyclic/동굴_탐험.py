# https://programmers.co.kr/learn/courses/30/lessons/67260?language=python3

# solution 1 : recursion

import sys
sys.setrecursionlimit(1000000)

from collections import defaultdict

def solution(n, path, order):
    
    graph = defaultdict(list)
    for i, j in path:
        graph[i].append(j)
        graph[j].append(i)
    
    directed_graph = defaultdict(list)
    stack = [0]
    visited = [0]*n
    
    while stack:
        i = stack.pop()
        visited[i] = 1
        for j in graph[i]:
            if visited[j] == 0:
                directed_graph[i].append(j)
                stack.append(j)
    
    for i, j in order:
        directed_graph[i].append(j)
    
    stack = [0]
    visited = [0]*n
    visiting = [0]*n
    
    def is_tree(i):
        visited[i] = 1
        visiting[i] = 1
        for j in directed_graph[i]:
            if visiting[j]:
                return False
            if visited[j] == 0 and not is_tree(j):
                return False
        visiting[i] = 0
        return True
    
    return is_tree(0)

# solution 2: iteration

from collections import defaultdict

def solution(n, path, order):
 
    graph = defaultdict(list)
    requirement = {}
    unlock = {}
    
    for node1, node2 in path:
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    for node1, node2 in order:
        requirement[node2] = node1
        unlock[node1] = node2
    
    visited = [0]*n
    stack = [0]
    plan = set()

    while stack:
        curr = stack.pop()
        
        # 방문 조건이 만족 안되는 경우
        if curr in requirement and visited[requirement[curr]] == 0:
            plan.add(requirement[curr])
            continue
        
        # 방문 조건 만족한 경우
        visited[curr] = 1
        for node in graph[curr]:
            if visited[node] == 0:
                stack.append(node)
        
        if curr in plan:
            stack.append(unlock[curr])
            plan.remove(curr)

    return not plan