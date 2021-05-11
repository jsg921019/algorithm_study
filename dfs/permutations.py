# https://leetcode.com/problems/permutations/submissions/
# Easy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(l, s):
            if s:
                for n in s:
                    dfs(l+[n], s-{n})
            else:
                answer.append(l)
                
        answer = []
        dfs([], set(nums))
        
        return answer