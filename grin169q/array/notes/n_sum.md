# N Sum
Involved Questions: 1, 15, 16
## 1 - Two Sum
Given an array of integers _nums_ and an integer _target_, return indices of the two numbers such that they add up to 
_target_ (assume only exactly one solution).

### 1.1 Two Pointer Solution
The idea is to sort the array, set two pointers respectively at the two ends of the array, and move them towards the middle of the array.
``` 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []
```
### 1.2 Two Sum with Multiple Solutions
The **difficulty** of this version is that all returned elements should not have duplication.

To avoid duplication, we need to skip all duplicated elements when checking if sum == target.
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            cur_left = nums[left]
            cur_right = nums[right]
            if cur_left + cur_right == target:
                res.append([left, right]) 
                while left < right and nums[left] == cur_left:
                    left += 1
                while left < right and nums[right] == cur_right:
                    right -= 1
            elif cur_left + cur_right < target:
                while left < right and nums[left] == cur_left:
                    left += 1
            else:
                while left < right and nums[right] == cur_right:
                    right -= 1
        return res
```

## 2 - Three Sum
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`,
and `j != k`, and `nums[i] + nums[j] + nums[k] == 0` (solution set must not contain duplicate triplets).
``` 
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
```















