# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         ans = 0
#         n = len(s)
#         left, right = 0, 0
#         uniq_chars = set()

#         while left < n and right < n:
#             if s[right] not in uniq_chars:
#                 uniq_chars.add(s[right])
#                 right += 1
#                 ans = max(ans, right - left)
#             else:
#                 uniq_chars.remove(s[left])
#                 left += 1
#         print(ans)
#         return ans

        

# s = "pwwkew"
# sol = Solution().lengthOfLongestSubstring(s)


# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
#         lenght1 = len(nums1)
#         lenght2 = len(nums2)

#         if not lenght1:
#             if lenght1%2 == 0:
#                 return nums1[lenght1//2]
#             else:
#                 return (nums1[lenght1//2] + nums1[lenght1//2]) / 2 

#         # print(n//2, m//2)

# nums1 = [1,2]
# nums2 = [3,4]

# nums1 = [1,3]
# nums2 = [2]

# sol = Solution()
# sol.findMedianSortedArrays(nums1, nums2)



strs = ["flower","flow","flight"]

class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word_count = 0

    def insert(self, root, key):
        cur_node = root

        for char in key:
            if cur_node.childNode[ord(char) - ord('a')] == None:
                new_node = TrieNode()
                 


