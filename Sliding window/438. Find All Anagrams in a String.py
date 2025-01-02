class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        arr = []
        p_dict = {}
        for char in p:
            p_dict[char] = p_dict.get(char, 0) + 1

        end = 0
        s_dict = {}
        for start in range(len(s) - len(p) + 1):
            
            while end - start < len(p):
                if s[end] in p_dict.keys():
                    s_dict[s[end]] = s_dict.get(s[end], 0) + 1
                end += 1
            
            if s_dict == p_dict:
                arr.append(start)
            
            if s[start] in p_dict.keys():
                s_dict[s[start]] -= 1

        return arr


s = "cbaebabacd"
p = "abc"

s = "abab"
p = "ab"

s = "ababababab"
p = 'aab'

sol = Solution()
sol.findAnagrams(s, p)
