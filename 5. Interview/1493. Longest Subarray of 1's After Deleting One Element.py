class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        
        ans = 0
        left = 0
        zero_count = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left)
        return ans 

            


nums = [1,1,0,1]

# nums = [0,1,1,1,0,1,1,0,1]

# nums = [1,1,1]

sol = Solution()
sol.longestSubarray(nums)