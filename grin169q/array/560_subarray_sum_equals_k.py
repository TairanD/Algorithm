from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = result = 0
        # key: sum; value: index (location) of the current index
        prefix = {0: 1}
        for index, num in enumerate(nums):
            sum += num
            diff = sum - k
            if diff in prefix:
                result += prefix[diff]
            if sum not in prefix:
                prefix[sum] = 1
            else:
                prefix[sum] += 1
        return result

print(Solution().subarraySum([1,1,1],2))