class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        res = 0
        left = -1

        for right in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            if k < 0:
                left += 1
                if nums[left] == 0:
                    k += 1

            res = max(res, right - left)
        
        return res



nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

sol = Solution()
sol.longestOnes(nums, k)