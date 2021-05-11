# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Easy

class Solution:
    
    d = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
         '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        output = []
        def dfs(s):
            if len(s) == len(digits):
                output.append(s)
                return
            next_num = digits[len(s)]
            for next_letter in self.d[next_num]:
                dfs(s+next_letter)
        dfs('')
        return output

a= Solution()
print(a.letterCombinations('23'))