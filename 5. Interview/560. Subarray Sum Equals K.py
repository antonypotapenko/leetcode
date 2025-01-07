class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        
        count = 0
        prefix_sum = 0
        prefix_dict = {0:1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_dict:
                count += prefix_dict[prefix_sum - k]
            
            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

        return count

nums = [1,1,1]
k = 2

nums = [1,2,3]
k = 3

nums = [1,2,1,2,1]
k = 3


sol = Solution()
sol.subarraySum(nums, k)