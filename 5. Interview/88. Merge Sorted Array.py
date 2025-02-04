class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        
        index1, index2 = m - 1, n - 1
        cur_index = n + m - 1

        while index2 >= 0:
            
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[cur_index] = nums1[index1]
                index1 -= 1

            else:
                nums1[cur_index] = nums2[index2]
                index2 -= 1

            cur_index -= 1

        
            


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3

nums1 = [0]
m = 1
nums2 = [1]
n = 1

sol = Solution()
sol.merge(nums1, m, nums2, n)