class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for idx in range(n):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = n - 1

            while left < right:

                three_sum = nums[idx] + nums[left] + nums[right]

                if three_sum == 0:
                    ans.append([nums[idx], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif three_sum < 0:
                    left += 1

                else:
                    right -= 1

            return ans



nums = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]
nums = [0,1,1] # []
nums = [0,0,0] # [[0,0,0]]
nums = [0,0,0,0] # [[0,0,0]]



sol = Solution()
sol.threeSum(nums)
