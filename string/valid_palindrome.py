# https://leetcode.com/problems/valid-palindrome/

# solution 1: using regex

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-z0-9]','', s.lower())
        return s == s[::-1]

# solution 2: using translate

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('','',string.punctuation + ' ')).lower()
        return s == s[::-1]

# solution 3 : using list

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [s_ for s_ in s.lower() if s_.isalnum()]
        return s == s[::-1]