class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        ans = 0
        jew_set = set(jewels)

        for char in stones:
            if char in jew_set:
                ans += 1
        
        return ans



jewels = "aA"
stones = "aAAbbbb"

jewels = "z"
stones = "ZZ"

sol = Solution()
sol.numJewelsInStones(jewels, stones)