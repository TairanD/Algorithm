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