class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        if k <= 1:
            return 0

        left = 0
        count = 0
        power = 1
        n = len(nums)

        for right in range(n):
            
            power *= nums[right]

            while power >= k and left <= right:
                power /= nums[left]
                left += 1
            
            count += (right - left + 1)

        return count


nums = [10,5,2,6]
k = 100

nums = [1,2,3]
k = 0

sol = Solution()
sol.numSubarrayProductLessThanK(nums, k)