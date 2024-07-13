from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize each position as 0
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                result[i] = index - i
            stack.append(index)
        return result


"""
Note:
The overall thinking of this question is to initialize all elements to 0, and maintaining the elements in the stack is 
descending (in this way, we do not need to change them). When we encounter one element greater than the stack.pop(), we 
begin popping all such elements to maintain the descending stack.
"""
