class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        n = len(nums)
        if not n:
            return 0
        
        end = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[end] = nums[i]
                end += 1
        return end



nums = [1,1,2]

nums = [0,0,1,1,1,2,2,3,3,4]

nums = [1, 2]

nums = [1]

sol = Solution()
sol.removeDuplicates(nums)