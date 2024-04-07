# O(N*log N) Sorting Method

## 1 - MergeSort
Procedure:
1. Divide: The input array is divided into two halves. This process continues recursively until each subarray contains 
only one element.
2. Base: Once the subarrays contain only one element, they are considered sorted. 
3. Recursive Call mergeSort function
4. Merge: During the merge operation, the elements of two sorted subarrays are compared and merged into a single sorted array.

Why MergeSort is more efficient? - Because it does not a lot of comparison operations (unlike the previous algorithms).

*Note: recursion process can be viewed as a tree with some kind of traversal.
## 2 - Small Sum

## 3 - Inverse Pair

## 4 - Flag of the Netherlands
### 4.1 - Q1
Given an int[] _arr_ and a number _num_, sort the elements less than or equal to  _num_ on the left side of _num_, the elements greater
than _num_ on the right side. Require the space complexity is O(1), the time complexity is O(N).

### 4.2 - Q2. Flag of the Netherlands
Given an int[] _arr_ and a number _num_, sort the elements less than _num_ on the left side, the elements equal to _num_ in the middle, 
the elements greater than _num_ on the right side. Require the space complexity is O(1), the time complexity is O(N).

## 5 - QuickSort