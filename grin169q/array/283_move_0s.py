class Solution(object):
    def swap(self, i1, i2, arr):
        temp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = temp

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        first_0 = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] != 0:
                self.swap(cur, first_0, nums)
                first_0 += 1
            cur += 1
        return nums