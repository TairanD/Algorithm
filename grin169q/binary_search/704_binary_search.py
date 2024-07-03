class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        search_start = 0
        search_end = len(nums) - 1
        while search_start <= search_end:
            mid = (search_end + search_start) // 2
            if nums[mid] < target:
                search_start = mid + 1
            elif nums[mid] > target:
                search_end = mid - 1
            else:
                return mid
        return -1
