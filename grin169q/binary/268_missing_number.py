class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        complete = range(len(nums)+1)
        res = 0
        for i in range(0, len(nums)):
            res ^= complete[i] ^ nums[i]
        return res ^ complete[-1]