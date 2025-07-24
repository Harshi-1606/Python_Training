class Solution:
    def letterCasePermutation(s):
        res = [""]
        for char in s:
            if char.isalpha():
                res = [prefix + char.lower() for prefix in res] + [prefix + char.upper() for prefix in res]
            else:
                res = [prefix + char for prefix in res]
        return res

sol = Solution()
print(sol.letterCasePermutation('a1b1'))


