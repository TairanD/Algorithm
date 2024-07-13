class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        res = 0
        for char in tokens:
            if char in ['+', '-', '*', '/']:
                num1 = stack.pop()
                num2 = stack.pop()
                if char == '+':
                    res = num1 + num2
                elif char == '-':
                    res = num2 - num1
                elif char == '*':
                    res = num1 * num2
                elif char == '/':
                    res = int(num2 / num1)
                stack.append(int(res))
            else:
                stack.append(int(char))
            print(f"stack: {stack}")
            print(f"res: {res}")
        return res
print(int(6/-132))
# print(Solution().evalRPN(`["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))