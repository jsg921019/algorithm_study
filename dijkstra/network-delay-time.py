# https://leetcode.com/problems/network-delay-time/submissions/

# solution 1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        path = defaultdict(list)
        for u, v, w in times:
            path[u].append((v, w))
        
        dists = {}
        hq = [(0, k)]
        
        while hq:
            curr_dist, curr_node = heappop(hq)
            if curr_node in dists:
                continue
            dists[curr_node] = curr_dist 
            for next_node, dist in path[curr_node]:
                if next_node in dists:
                    continue
                heappush(hq, (curr_dist+dist, next_node))
            if len(dists) == n:
                return max(dists.values())
        else:
            return -1

# solution 2

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:dict() for i in range(1, n+1)}
        for u,v,w in times:
            graph[u][v] = w
            
        dist = [float('inf') for i in range(n+1)]
        dist[0], dist[k] = 0, 0
        visited = [False]*(n+1)
        
        queue = [(0, k)]
        
        while len(queue):
            minNode = heappop(queue)[1]
            if visited[minNode]: continue
            visited[minNode] = True
            for node in graph[minNode]:
                if not visited[node] and dist[minNode] + graph[minNode][node] < dist[node]:
                    dist[node] = dist[minNode] + graph[minNode][node]
                    heappush(queue, (dist[node], node))
        
        ans = max(dist)
        return ans if ans != float('inf') else -1