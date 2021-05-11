# https://leetcode.com/problems/valid-parentheses/

# Easy

class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        l = []
        for s_ in s:
            if s_ in d:
                l.append(s_)
            elif not(l and d[l.pop()] == s_):
                return False
        return len(l) == 0