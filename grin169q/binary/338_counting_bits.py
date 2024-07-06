class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [bin(i).count("1") for i in range(n+1)]
    """
    In such way, the time complexity is O(n * length of binary i), adopting dynamic programming is more efficient
    """