class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        left = 0
        right = 0
        counter = 0
        bug = set()


        while right < len(fruits):

            if fruits[right] not in bug and not bug:
                bug.add(fruits[right])
                right += 1

            elif fruits[right] not in bug:
                counter = max(counter, right - left)

                while fruits[left] in bug:
                    bug.remove(fruits[left])
                    left += 1
                bug.add(fruits[right])
            
            counter = max(counter, right - left)
            right += 1

        print(counter)



fruits = [1,2,2]
# fruits = [0,1,2,2]

sol = Solution()
sol.totalFruit(fruits)