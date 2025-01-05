class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        n = len(height)
        left = 0
        right = n - 1
        area = 0

        while left < right:

            if height[left] <= height[right]:
                area = max(area, height[left]*(right-left))
                left += 1

            else:
                area = max(area, height[right]*(right-left))
                right -= 1

        return area

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

sol = Solution()
sol.maxArea(height)