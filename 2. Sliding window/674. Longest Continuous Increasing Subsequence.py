class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        cur_len = 1

        for start in range(1, len(nums)):

            if nums[start] > nums[start-1]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1

        return max_len


nums = [1,3,5,4,7]
nums = [2,2,2,2,2]

sol = Solution()
sol.findLengthOfLCIS(nums)
