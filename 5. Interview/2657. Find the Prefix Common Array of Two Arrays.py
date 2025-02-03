class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        
        n = len(A)
        count = [0] * (n + 1)

        prefix = 0
        result = [] 

        for index in range(n):
            count[A[index]] += 1
            if count[A[index]] == 2:
                prefix += 1
            
            count[B[index]] += 1
            if count[B[index]] == 2:
                prefix += 1

            result.append(prefix)

        return result
    
A = [2,3,1]
B = [3,1,2]

sol = Solution()
sol.findThePrefixCommonArray(A,B)
