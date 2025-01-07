class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointer_s = 0
        pointer_t = 0

        while pointer_t < len(t):
            
            if pointer_s < len(s) and s[pointer_s] == t[pointer_t]:
                pointer_s += 1
            pointer_t += 1

        return pointer_s == len(s)

s = "abc"
t = "ahbgdc"

s = "axc"
t = "ahbgdc"

s = "b"
t = 'abc'

sol = Solution()
sol.isSubsequence(s,t)