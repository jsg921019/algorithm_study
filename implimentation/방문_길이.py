# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    
    d = {'U':(1,0), 'D':(-1,0), 'R':(0,1), 'L':(0,-1)}
    path = set()
    x, y = 0, 0
    for cmd in dirs:
        dx, dy = d[cmd]
        if -5 <= x+dx <=5 and -5 <= y+dy <= 5:
            path.add((min(x, x+dx), min(y, y+dy), dx == 0))
            #path.add((x, y, x+dx, y+dy))
            #path.add((x+dx, y+dy, x, y))
            x, y = x + dx, y + dy
    
    return len(path) #// 2