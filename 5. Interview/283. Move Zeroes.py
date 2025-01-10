class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeros = 0
        left = 0

        for right in range(n):

            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            else:
                zeros += 1

        for idx in range(zeros):
            nums[n - idx - 1] = 0
        
        print(nums)



nums = [0,1,0,3,12]
nums = [0]

sol = Solution()
sol.moveZeroes(nums)