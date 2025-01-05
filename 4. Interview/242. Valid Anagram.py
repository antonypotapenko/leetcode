class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        len_s = len(s)
        len_t = len(t)
        dict_s, dict_t = {}, {}

        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        if len_s == len_t and dict_s == dict_t:
            return True

        return False


s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

s = "aacc"
t = "ccac"

sol = Solution()
sol.isAnagram(s, t)