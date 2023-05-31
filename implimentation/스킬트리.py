# https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3

def solution(skill, skill_trees):
    
    answer = 0
    skill_set = set(skill)

    for skill_tree in skill_trees:
        x = ''.join([c for c in skill_tree if c in skill_set])
        if skill.startswith(x):
            answer += 1
    
    return answer