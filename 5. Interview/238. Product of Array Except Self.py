class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        result = [1] * n
        
        power = 1
        for i in range(n):
            result[i] *= power
            power *= nums[i]

        power = 1
        for i in range(n-1,-1,-1):
            result[i] *= power
            power *= nums[i]
        
        return result



nums = [1,2,3,4]

nums = [-1,1,0,-3,3]

sol = Solution()
sol.productExceptSelf(nums)