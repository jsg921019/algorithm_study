# https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/

from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))
        hq = [(0, -1, src)]
        visited = set()
        
        while hq:
            tot_cost, tot_step, city = heappop(hq)
            
            if city in visited or tot_step > K:
                continue
                
            if city == dst:
                return tot_cost
            
            visited.add((city, tot_step))
            for next_city, cost in graph[city]:
                if (next_city, tot_step) not in visited:
                    heappush(hq, (tot_cost+cost, tot_step+1, next_city))

        return -1