class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        res = 0
        stack = []
        operators = set('+-*/')

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:

            if token not in operators:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '/':
                    res = int(left / right)
                else:
                    res = left * right
            
                stack.append(res)

        return res
        


# tokens = ["2","1","+","3","*"]

tokens = ["4","13","5","/","+"]

# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

tokens = ["18"]

tokens = ["4","3","-"]

# tokens = ["3","11","+","5","-"]

sol = Solution()
sol.evalRPN(tokens)