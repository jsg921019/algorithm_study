# https://leetcode.com/problems/trapping-rain-water/submissions/

# solution 1: using two pointer

class Solution:
    def trap(self, height: List[int]) -> int:

        answer = 0
        head, tail = 0, len(height)-1
        head_max, tail_max = 0, 0

        while head <= tail:
            if head_max < tail_max:
                if height[head] > head_max:
                    head_max = height[head]
                else:
                    answer += head_max - height[head]
                head += 1
            else:
                if height[tail] > tail_max:
                    tail_max = height[tail]
                else:
                    answer += tail_max - height[tail]
                tail -= 1

        return answer

# solution 2: using stack

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h > stack[-1][-1]:
                i1, h1 = stack.pop()
                if stack:
                    i2, h2 = stack[-1]
                    answer += (i - i2 - 1) * (min(h2, h) - h1)
            stack.append((i, h))
        return answer