class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        arr = []
        n = len(nums)

        if n == 0:
            return []

        start = nums[0]
        
        for index in range(1, n):

            if nums[index-1] + 1 != nums[index]:
                if start == nums[index-1]:
                    arr.append(f'{start}')
                else:
                    arr.append(f'{start}->{nums[index-1]}')
                start = nums[index]
        
        if start == nums[-1]:
            arr.append(str(nums[-1]))
        else:
            arr.append(f'{start}->{nums[-1]}')

        return arr




nums = [0,1,2,4,5,7]
# nums = [0,2,3,4,6,8,9]
# nums = [1]
# nums = []

sol = Solution()
sol.summaryRanges(nums)