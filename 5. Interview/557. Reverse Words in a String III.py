class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.split(" "))
        res = []
        for word in arr:
            res.append(word[::-1])
        return " ".join(res)
        

s = "Let's take LeetCode contest"

# s = "Mr Ding"

sol = Solution()
sol.reverseWords(s)