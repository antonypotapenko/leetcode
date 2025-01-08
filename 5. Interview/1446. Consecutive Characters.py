class Solution:
    def maxPower(self, s: str) -> int:

        if not s:
            return 0

        count = 1
        cur_count = 1
        for index in range(1, len(s)):

            if s[index] == s[index-1]:
                cur_count += 1

            if s[index] != s[index-1]:
                count = max(cur_count, count)
                cur_count = 1
        
        return max(count, cur_count)


s = "leetcode"
# s = "abbcccddddeeeeedcba"
s = 'cc'

sol = Solution()
sol.maxPower(s)