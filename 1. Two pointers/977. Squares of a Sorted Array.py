class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        left = 0
        right = n - 1
        arr = [0] * n
        pos = n - 1

        while left <= right:

            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                arr[pos] = left_square
                left += 1
            else:
                arr[pos] = right_square
                right -= 1
            
            pos -= 1

        return arr


nums = [-4,-1,0,3,10]

nums = [-7,-3,2,3,11]

nums = [1]

nums = [-5,-3,-2,-1]

sol = Solution()
sol.sortedSquares(nums)