# https://programmers.co.kr/learn/courses/30/lessons/42860#

def solution(name):

    l = [min(ord('Z') - ord(c) + 1, ord(c) - ord('A')) for c in name]
    not_A = [i for i, n in enumerate(l) if n]
    
    if not not_A :
        return 0

    rl = [2*i1 + len(l) - i2 for i1, i2 in zip([0]+not_A[:1], not_A)]
    lr = [2*(len(l)-i1) + i2 for i1, i2 in zip(not_A[1:]+[len(l)], not_A)]

    return min(lr+rl) + sum(l)