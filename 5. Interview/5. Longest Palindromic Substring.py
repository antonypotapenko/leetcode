class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ''
        n = len(s)

        for idx in range(n):

            left, right = idx, idx
            while left >= 0 and right < n and s[left] == s[right]:

                if len(ans) < right - left + 1 :
                    ans = s[left:right+1]
                left -= 1
                right += 1

            left, right = idx, idx + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if len(ans) < right - left + 1:
                    ans = s[left:right+1]
                left -= 1
                right += 1

        return ans



s = "babad"
s = "cbbd"
s = 'a'

sol = Solution()
sol.longestPalindrome(s)