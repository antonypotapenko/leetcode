class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        left = 0
        dct = {}
        counter = 0
        
        for right, fruit in enumerate(fruits):
            
            dct[fruit] = dct.get(fruit, 0) + 1

            while len(dct) > 2:
                dct[fruits[left]] -= 1
                
                if dct[fruits[left]] == 0:
                    del dct[fruits[left]]

                left += 1

            counter = max(counter, right - left + 1)
        
        return counter


fruits = [1,2,2]

fruits = [0,1,2,2]

sol = Solution()
sol.totalFruit(fruits)