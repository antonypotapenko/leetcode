class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        start = 0
        substr = set()

        for char in s:
            if char not in substr:
                substr.add(char)
            else:
                while char in substr and s[start] in substr:
                    substr.remove(s[start])
                    start += 1
                
                substr.add(char)
            ans = max(ans, len(substr))
                
        return ans
            

s = "abcabcbb" # ans = 3
s = "bbbbb" # 1
s = "pwwkew" # 3
s = "dvdf" # 3

sol = Solution()
sol.lengthOfLongestSubstring(s)
