class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for char in s:
            if char != "#":
                stack_s.append(char)
            else:
                if stack_s:
                    stack_s.pop()
        for char in t:
            if char != "#":
                stack_t.append(char)
            else:
                if stack_t:
                    stack_t.pop()

        return stack_s == stack_t