class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        ans = float('inf')
        left = 0
        right = 0
        summary = 0

        for right in range(len(nums)):
            
            summary += nums[right]
            while summary >= target:
                ans = min(ans, right - left + 1)
                summary -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0
        return ans


target = 7
nums = [2,3,1,2,4,3]

target = 4
nums = [1,4,4]

target = 11
nums = [1,1,1,1,1,1,1,1]

sol = Solution()
sol.minSubArrayLen(target, nums)
