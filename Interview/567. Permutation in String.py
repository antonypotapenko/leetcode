class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dict1 = {}
        for char in s1:
            dict1[char] = dict1.get(char, 0) + 1
        
        end = 0
        dict2 = {}
        for start in range(len(s2) - len(s1) + 1):

            while end - start < len(s1):
                if s2[end] in dict1.keys():
                    dict2[s2[end]] = dict2.get(s2[end], 0) + 1
                end += 1

            if dict1 == dict2:
                return True

            if s2[start] in dict2.keys():
                dict2[s2[start]] -= 1

        return False

s1 = "ab"
s2 = "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

sol = Solution()
sol.checkInclusion(s1, s2)