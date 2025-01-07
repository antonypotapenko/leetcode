class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        ans = []
        last_index = {}
        for index, char in enumerate(s):
            last_index[char] = index

        start, end = 0, 0
        for index, char in enumerate(s):
            end = max(end, last_index[char])

            if index == end:
                ans.append(end - start + 1)
                start = index + 1

        return ans



s = "ababcbacadefegdehijhklij" # "ababcbaca defegde hijhklij"

# s = "eccbbbbdec"

sol = Solution()
sol.partitionLabels(s)