# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def backtrack(current, total):
            if current + total == num:
                return True
            base = 10
            while base < current:
                if backtrack(current // base, total + current % base):
                    return True
                base *= 10
            return False
        
        ans = 0
        for num in range(1, n + 1):
            squared = num * num
            if backtrack(squared, 0):
                ans += num * num
        return ans
