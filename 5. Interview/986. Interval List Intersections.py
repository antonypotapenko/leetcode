class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:

        arr = []
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(firstList) and pointer2 < len(secondList):

            start1, end1 = firstList[pointer1]
            start2, end2 = secondList[pointer2]

            start_inersection = max(start1, start2)
            end_intersection = min(end1, end2)

            if start_inersection <= end_intersection:
                arr.append([start_inersection, end_intersection])

            if end1 < end2:
                pointer1 += 1
            else:
                pointer2 += 1

        return arr
            




firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

# firstList = [[1,3],[5,9]]
# secondList = []

sol = Solution()
sol.intervalIntersection(firstList, secondList)