class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        ans = 0
        left = 0

        for right in range(len(nums)):

            while ans < k:
                ans += nums[right]
            
            pass







nums = [1,1,1]
k = 2

nums = [1,2,3]
k = 3


sol = Solution()
sol.subarraySum(nums, k)