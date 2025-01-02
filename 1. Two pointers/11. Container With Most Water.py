class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            if height[left] < height[right]:
                ans = max(ans, (right - left)*height[left])
                left += 1
            else:
                ans = max(ans, (right - left)*height[right])
                right -= 1
                
        return ans
            

height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]

sol = Solution()
sol.maxArea(height)