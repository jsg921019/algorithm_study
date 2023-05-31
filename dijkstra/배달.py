# https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3

from heapq import heappush, heappop

def solution(N, road, K):

    dist_mtx = [[K+1]*N for _ in range(N)]
    for a, b, c in road:
        dist_mtx[a-1][b-1] = min(dist_mtx[a-1][b-1], c)
        dist_mtx[b-1][a-1] = min(dist_mtx[b-1][a-1], c)

    hq = [(0,0)]
    visited = set()
    
    while hq:
        dist, town = heappop(hq)

        if town in visited:
            continue

        visited.add(town)
        for town_, dist_ in enumerate(dist_mtx[town]):
            if town_ not in visited and dist+dist_ <= K:
                heappush(hq, (dist+dist_, town_))

    return len(visited)