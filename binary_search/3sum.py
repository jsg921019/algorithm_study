# https://leetcode.com/problems/3sum/submissions/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []

        answer = []
        count = Counter(nums)
        nums = sorted(count)

        for i1, num1 in enumerate(nums):

            if num1 > 0:
                break

            num2_min, num2_max = -num1-nums[-1], -num1/2
            lo = bisect_left(nums, num2_min, i1 + 1)
            hi = bisect_left(nums, num2_max, lo)

            for num2 in nums[lo:hi]:
                num3 = -num1 - num2
                if num3 in count:
                    answer.append((num1, num2, num3))

        for num in nums:
            if count[num] > 1:
                if num == 0 and count[num] >= 3:
                    answer.append((num, num, num))
                elif num != 0 and 0 - 2 * num in count:
                    answer.append((num, num, 0 - 2 * num))
                    
        return answer