from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        # entries in d: {cumulative sum, first csum index}
        d = {0: -1}
        csum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                csum -= 1
            else:
                csum += 1
            if csum in d:
                ans = max(ans, i - d[csum])
            else:
                d[csum] = i
        return ans
