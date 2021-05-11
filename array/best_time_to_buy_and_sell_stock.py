# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        answer = 0
        for p in prices[1:]:
            if p - min_p > answer:
                answer = p - min_p
            if p < min_p:
                min_p = p
        return answer