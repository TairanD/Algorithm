from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        minimum = float('inf')
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            cur = nums[index]
            i = index + 1
            j = len(nums) - 1

            while i < j:
                total = cur + nums[i] + nums[j]
                if minimum > abs(target - total):
                    minimum = abs(target - total)
                    ans = total

                if total < target:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif total > target:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    return target
        return ans


Solution().threeSumClosest([1, 3, 4, 7, 8, 9], 15)
