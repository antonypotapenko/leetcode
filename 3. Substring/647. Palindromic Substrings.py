class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        # odd substrings
        for idx in range(n):
            left = idx
            right = idx

            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1

                left -= 1
                right += 1
        
            # even substrings
            left = idx
            right = idx + 1

            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1

                left -= 1
                right += 1
        return ans



s = "abc"
s = "aaa"
s = "fdsklf"

sol = Solution()
sol.countSubstrings(s)
