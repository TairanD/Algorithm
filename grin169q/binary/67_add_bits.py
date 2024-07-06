class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        total = carry = 0
        a, b = a[::-1], b[::-1]
        result = ''
        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord('0') if i < len(a) else 0
            digit_b = ord(b[i]) - ord('0') if i < len(b) else 0
            total = digit_a + digit_b + carry
            result = str(total % 2) + result
            carry = total >> 1
        if carry:
            result = '1' + result
        return result