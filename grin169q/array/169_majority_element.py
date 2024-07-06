class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_dict = {}

        for num in nums:
            if num not in element_dict:
                element_dict[num] = 1
            else:
                element_dict[num] += 1
            if element_dict[num] > (len(nums)-1)//2:
                return num
        return None