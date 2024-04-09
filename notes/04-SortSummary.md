# Sort Summary

## Stability of Algorithm

Stability means that equivalent elements retain their relative positions, after sorting.

## Summary

|               | Time complexity | Space Complexity | Stability |
|---------------|-----------------|------------------|-----------|
| SelectionSort | O(N^2)          | O(1)             | false     |
| BubbleSort    | O(N^2)          | O(1)             | true      |
| InsertionSort | O(N^2)          | O(1)             | true      |
| MergeSort     | O(N*logN)       | O(N)             | true      |
| **QuickSort** | O(N*logN)       | O(log N)         | false     |
| HeapSort      | O(N*logN)       | O(1)             | false     |

## Sort Improvement in Engineering
1. Comprehensive Sort Algorithm
   - For example, quickSort + selectionSort: combine the advantages of two algorithms
2. Library Array.sort() will 
   1. use quickSort to sort primitive values - faster
   2. use mergeSort to sort customized objects - more stable