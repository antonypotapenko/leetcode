class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        prefix_sum = 0
        prefix_dict = {0:-1}

        for idx, num in enumerate(nums):
            pass




nums = [23,2,4,6,7]
k = 6

nums = [23,2,6,4,7]
k = 6

nums = [23,2,6,4,7]
k = 13

nums = [0]
k = 1

sol = Solution()
sol.checkSubarraySum(nums, k)