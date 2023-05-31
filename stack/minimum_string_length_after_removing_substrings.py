# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution:
    def minLength(self, s: str) -> int:
        pair = {"B": "A", "D": "C"}
        stack = []
        for c in s:
            if stack and c in pair and stack[-1] == pair[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
