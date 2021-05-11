# https://leetcode.com/problems/most-common-word/

import collections, re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = [word for word in re.split('[ !?\',;.]+',  paragraph.lower()) if word not in banned]
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]