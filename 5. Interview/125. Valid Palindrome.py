from string import ascii_lowercase

class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = set(ascii_lowercase + '0123456789')
        palindrome = ''
        for char in s:
            tmp = char.lower()
            if tmp in chars:
                palindrome += tmp
        
        n = len(palindrome)
        if n <= 1:
            return True
        
        left = 0
        right = n - 1
        while left < right:
            if palindrome[left] != palindrome[right]:
                return False
            left += 1
            right -= 1

        return True

s = "A man, a plan, a canal: Panama"

s = "race a car"

s = " "

s = 'ab'

s = "0P"

sol = Solution()
sol.isPalindrome(s)