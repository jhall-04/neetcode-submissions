class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        nums = '1234567890'
        for token in tokens:
                if token == '+':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a+b)
                elif token == '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a-b)
                elif token == '*':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a*b)
                elif token == '/':
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a/b))
                else:
                    stack.append(int(token))
        return int(stack[-1])
                

            
        