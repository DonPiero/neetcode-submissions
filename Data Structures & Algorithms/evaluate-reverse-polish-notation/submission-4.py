class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '/':
                helper = stack.pop()
                stack.append(int(stack.pop() / helper))
            elif i == '*':
                helper = stack.pop()
                stack.append(stack.pop() * helper)
            elif i == '-':
                helper = stack.pop()
                stack.append(stack.pop() - helper)
            elif i == '+':
                helper = stack.pop()
                stack.append(stack.pop() + helper)
            else:
                stack.append(int(i))
        
        return stack[-1]
                
