class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_vals ={}
        for idx, num in enumerate(nums):
            if target - num in dict_vals:
                return [dict_vals[target-num], idx]
            dict_vals[num] = idx
            


nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

sol = Solution()
sol.twoSum(nums, target)