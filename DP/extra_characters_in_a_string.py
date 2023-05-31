# https://leetcode.com/problems/extra-characters-in-a-string/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        lengths = sorted(set(len(w) for w in dictionary))
        words = set(dictionary)

        dp = [0]

        for i in range(1, len(s)+1):
            dp.append(dp[-1] + 1)
            for l in lengths:
                if l > i:
                    break
                if s[len(s)-i: len(s)-i+l] in words:
                    dp[-1] = min(dp[-1], dp[-1-l])

        return dp[-1]
