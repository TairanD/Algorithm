from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if target - num not in dict:
                dict[num] = i
            else:
                return [i, dict[target - num]]
        return []