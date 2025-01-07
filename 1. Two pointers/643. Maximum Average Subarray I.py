class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        left = 0
        right = k
        cur_average = sum(nums[left:right])
        max_average = cur_average

        while right < len(nums):
            cur_average = cur_average - nums[left] + nums[right]
            max_average = max(max_average, cur_average)

            left += 1
            right += 1

        return max_average / k



nums = [1,12,-5,-6,50,3]
k = 4

nums = [5]
k = 1

nums = [0,4,0,3,2]
k = 1

sol = Solution()
sol.findMaxAverage(nums, k)