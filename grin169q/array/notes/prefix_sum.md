Involved Questions: 525, 560
# Prefix Sum
## 1 - What's Prefix Sum
A technique in cs used to allow for fast range sum queries (allowing fast querying the range sum of particular intervals).

The idea is to create an array where each element at index _i_ is the sum of all elements from the start
of the original array up to index _i_.

## 2 - Core Code
```
def prefix(nums):
    prefix = [0]
    sum = 0
    for i, num in nums:
        sum+=num
        prefix.append(sum)
    return prefix

# We can get the range sum with O(1) time complexity
def rangeSum(i, j, nums):
    prefix = prefix(nums)
    return prefix[j+1] - prefix[i]
```

## 3 - Q525: Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
```
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        # key: range sum ; value: index (location) this range sum firstly calulated
        prefix = {0: 0}
        max = 0
        
        for index, num in enumerate(nums):
            sum += num if num == 1 else -1
            if sum in prefix:
                max = max(max, index + 1 - prefix[sum])
            else: 
                prefix[sum] = index + 1
        return max
```

## 4 - 560: Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

``` 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = result = 0
        # key: sum; value: index (location) of the current index
        prefix = {0: 1}
        for index, num in enumerate(nums):
            diff = k - prefix_sum
            prefix_sum += num
            if diff in prefix:
                result += prefix[diff]
            if prefix_sum not in prefix:
                prefix[prefix_sum] = 1
            else: 
                prefix[prefix_sum] += 1
        return result
```




