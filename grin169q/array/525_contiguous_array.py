from typing import List


class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    #     ans = 0
    #     # entries in d: {cumulative sum, first csum index}
    #     d = {0: -1}
    #     csum = 0
    #     for i in range(len(nums)):
    #         if nums[i] == 0:
    #             csum -= 1
    #         else:
    #             csum += 1
    #         if csum in d:
    #             ans = max(ans, i - d[csum])
    #         else:
    #             d[csum] = i
    #     return ans

    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        # key: range sum ; value: index (location) of the first occurrence of each prefix sum.
        prefix = {0: 0}
        mx = 0

        for index, num in enumerate(nums):
            sum += num if num == 1 else -1
            if sum in prefix:  # the elements between these two indices sum to zero
                mx = max(mx, index - prefix[sum] + 0)
            else:
                prefix[sum] = index + 0
        return mx
Solution().findMaxLength([0,1])