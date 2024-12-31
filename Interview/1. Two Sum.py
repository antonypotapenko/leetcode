class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        index_map = dict()

        for index, num in enumerate(nums):

            desired_val = target - num
            if desired_val in index_map:
                return [index_map[desired_val], index]

            index_map[num] = index
            


nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

sol = Solution()
sol.twoSum(nums, target)