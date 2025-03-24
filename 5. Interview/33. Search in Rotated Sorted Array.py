class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        n = len(nums)
        left = 0
        right = n - 1
        

        def binary_search(left, right):
            mid = nums[(right-left)//2]
            if mid - left > 0:
                pass
            

        binary_search(left, right)





nums = [4,5,6,7,0,1,2]
target = 0

nums = [4,5,6,7,0,1,2]
target = 3

sol = Solution()
sol.search(nums, target)
