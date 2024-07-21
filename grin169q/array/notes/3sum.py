from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = 0
        while cur < len(nums):
            left = cur + 1
            right = len(nums) - 1
            cur_val = nums[cur]
            while left < right:
                left_val = nums[left]
                right_val = nums[right]
                if left_val + right_val == -cur_val:
                    res.append([cur_val, left_val, right_val])
                    while left < right and left_val == nums[left]:
                        left += 1
                    while left < right and right_val == nums[right]:
                        right -= 1
                elif left_val + right_val < -cur_val:
                    while left < right and left_val == nums[left]:
                        left += 1
                else:
                    while left < right and right_val == nums[right]:
                        right -= 1
            while cur < len(nums) and cur_val == nums[cur]:
                cur += 1
        return res

Solution().threeSum([-2,0,0,2,2])