class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []
        n = len(intervals)

        intervals.sort(key=lambda x:x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for index in range(1, n):

            cur_start = intervals[index][0]
            cur_end = intervals[index][1]

            if cur_start <= end:
                end = max(end, cur_end)

            else:
                ans.append([start, end])
                start = cur_start
                end = cur_end
        
        ans.append([start, end])
            
        return ans


intervals = [[1,3],[2,6],[8,10],[15,18]]

# intervals = [[1,4],[0,1]]

# intervals = [[1,4],[4,5]]

# intervals = [[1,4],[0,4]]

# intervals = [[1,4],[0,0]]

# intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

sol = Solution()
sol.merge(intervals)