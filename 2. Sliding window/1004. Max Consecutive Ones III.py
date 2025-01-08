class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        res = 0
        left = 0
        zero_count = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res



nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

sol = Solution()
sol.longestOnes(nums, k)