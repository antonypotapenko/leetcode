class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:

        distance = 0

        for cur_index in range(len(seats)):

            if seats[cur_index] == 0:
                left, right = cur_index, cur_index

                while left >= 0 and seats[left] == 0:
                    left -= 1
                while right < len(seats) and seats[right] == 0:
                    right += 1

                if cur_index == 0:
                    cur_distance = max(cur_index - left, right - cur_index)
                elif cur_index == len(seats) - 1:
                    cur_distance = max(cur_index - left, right - cur_index)
                else:
                    cur_distance = min(cur_index - left, right - cur_index)

                distance = max(distance, cur_distance)

        return distance



seats = [1,0,0,0,1,0,1]

seats = [1,0,0,0]

seats = [0,1]

sol = Solution()
sol.maxDistToClosest(seats)