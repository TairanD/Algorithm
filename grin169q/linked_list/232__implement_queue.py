class MyQueue(object):

    def __init__(self):
        self.stack = []

    # the idea is to put the new inserted element to the bottom of self.stack
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        temp1 = [x]
        # next, we need to copy the element in self.stack into temp1
        temp2 = []
        while self.stack:
            temp2.append(self.stack.pop())
        while temp2:
            temp1.append(temp2.pop())

        self.stack = temp1

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1] if not self.empty() else -1

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack

