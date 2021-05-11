# https://leetcode.com/problems/reconstruct-itinerary/submissions/

from collections import defaultdict
from bisect import insort
class Solution:
    def findItinerary(self, tickets):
        path = defaultdict(list)
        for x, y in sorted(tickets):
            path[x].append(y)
        answer = []
        def dfs(city):
            while path[city]:
                 dfs(path[city].pop(0))
            answer.append(city)
        dfs('JFK')
        return answer[::-1]