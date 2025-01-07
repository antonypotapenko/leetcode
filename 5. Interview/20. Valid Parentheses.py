class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) <= 1:
            return False

        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for char in s:
            
            if char not in brackets:
                stack.append(char)
            elif stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False

        return True if not stack else False



s = "()"
s = "()[]{}"
s = "(]"
s = "([])"
s = ']'
s = ")(){}"

sol = Solution()
sol.isValid(s)