# https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3

def solution(k, room_number):
    parents = {}
    answer = []
    for node in room_number:
        visited = [node]
        while node in parents:
            node = parents[node]
            visited.append(node)
        answer.append(node)
        for visited_node in visited:
            parents[visited_node] = node + 1
    return answer