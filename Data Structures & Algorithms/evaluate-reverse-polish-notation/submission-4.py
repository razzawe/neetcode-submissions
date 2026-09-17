class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {'+', '-', '*', '/'}
        numStack = []
        
        # computes tokens
        for i in range(len(tokens)):
            if tokens[i] in ops:
                if tokens[i] == '+':
                    num = int(numStack[-2]) + int(numStack[-1])
                    numStack.pop()
                    numStack.pop()
                    numStack.append(num)

                elif tokens[i] == '*':
                    num = int(numStack[-2]) * int(numStack[-1])
                    numStack.pop()
                    numStack.pop()
                    numStack.append(num)
                elif tokens[i] == '/':
                    num = int(numStack[-2]) / int(numStack[-1])
                    numStack.pop()
                    numStack.pop()
                    numStack.append(num)

                elif tokens[i] == '-':
                    num = int(numStack[-2]) - int(numStack[-1])
                    numStack.pop()
                    numStack.pop()
                    numStack.append(num)        

            else:
                numStack.append(tokens[i])
                print(numStack)
        return int(numStack[0])
            
