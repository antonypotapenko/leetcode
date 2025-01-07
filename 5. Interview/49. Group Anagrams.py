class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        return list(anagrams.values())



strs = ["eat","tea","tan","ate","nat","bat"]

strs = [""]

strs = ["a"]

sol = Solution()
sol.groupAnagrams(strs)
