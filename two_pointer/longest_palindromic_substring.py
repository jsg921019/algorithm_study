# https://leetcode.com/problems/longest-palindromic-substring/submissions/

# solution 1

class Solution:
    def longestPalindrome(self, s: str) -> str:

        head, tail = 0, 1
        answer = s[0]

        while tail < len(s):
            s_1 =  s[head-1:tail+1]
            s_2 = s[head:tail+1]
            if head and s_1 == s_1[::-1]:
                answer = s_1
                head -= 1
                tail += 1
            elif s_2 == s_2[::-1]:
                answer = s_2
                tail += 1
            else:
                head += 1
                tail += 1

        return answer

# solution 2

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1 or s == s[::-1]:
            return s
        
        start, maxlen = 0, 1
        
        for end in range(1, len(s)):
            sub1 = s[end-maxlen-1:end+1]
            sub2 = s[end-maxlen: end+1]
            
            if end-maxlen-1>=0 and sub1 == sub1[::-1]:
                start, maxlen = end-maxlen-1, maxlen+2
            elif end-maxlen>=0 and sub2 == sub2[::-1]:
                start, maxlen = end-maxlen, maxlen+1
        
        return s[start:start+maxlen]