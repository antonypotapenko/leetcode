class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        num_set = set(nums)
        for index in range(len(nums)+1):
            
            if index not in num_set:
                return index



nums = [3,0,1]
nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]

sol = Solution()
sol.missingNumber(nums)