# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def solution(p):
    
    # 1
    if not p:
        return p
    
    # 2
    cnt = 0
    flag = True
    for i, c in enumerate(p, 1):
        cnt += 1 if c == '(' else -1
        if cnt < 0:
            flag = False
        if cnt == 0:
            u, v = p[:i], p[i:]
    
             # 3
            if flag:
                return u + solution(v)

            # 4
            return '(' + solution(v) + ')' + ''.join([')' if c == '(' else '(' for c in u[1:-1]])