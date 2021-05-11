# https://leetcode.com/problems/remove-duplicate-letters/
# Medium

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        bag = set()
        l = [0]*len(s)
        for i, s_ in enumerate(s[::-1]):
            bag.add(s_)
            l[~i] = len(bag)
        q = []
        c = l[0]
        answer = []
        for s_, n in zip(s, l):
            if n != c:
                answer.extend(q)
                bag.update(q)
                c -= 1
                q = []
            if s_ not in answer and s_ not in q:
                if q and s_ < q[0]:
                    q = [s_]
                else:
                    q.append(s_)

        answer.extend(q)
        return ''.join(answer)

a = Solution()
print(a.removeDuplicateLetters("bcabcc"))