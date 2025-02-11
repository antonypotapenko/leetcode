# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7



# If you have rand_m()
# and you need find rand_n()
# you need to do:
#
#   def rand_m():
#       return random(1, m)
#   
#   def rand_n():
#       k = 1
#       power = m
#       
#       while power < n:
#           k += 1
#           power *= m
#       U = power - (power % n)
#
#       while True:
#           index = 0
#           for _ in range(k):
#               x = rand_m() - 1
#               index = index * m + x
#           
#           if index < U:
#               return (index % n) + 1
#


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
        while True:
            row = rand7() - 1
            col = rand7()

            val = row * 7 + col

            if val <= 40:
                return val % 10 + 1



n = 1

n = 2

n = 3

sol = Solution()
sol.rand10(n)