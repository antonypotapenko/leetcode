class Solution:
    def compress(self, chars: list[str]) -> int:
    
        count = 1
        cur_idx = 0

        for idx in range(1, len(chars) + 1):

            if idx < len(chars) and chars[idx] == chars[idx-1]:
                count += 1

            else:
                chars[cur_idx] = chars[idx-1]
                cur_idx += 1

                if count > 1:
                    for digit in str(count):
                        chars[cur_idx] = digit
                        cur_idx += 1
                count = 1

        return cur_idx




chars = ["a","a","b","b","c","c","c"]

chars = ["a"]

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

sol = Solution()
sol.compress(chars)