# Simple Sorting

In this file, 3 types of sorting algorithms (used to sort the order of a group of elements) will be introduced:
selection sort, bubble sort, and insertion sort.

## 0 - Method Swap()

The method takes three parameters:

1. the data structure containing elements.
2. the index of one of the elements waiting to swap.
3. the index of the other one.

## 1 - Selection Sorting

Procedure:
1. Find the minimum element in the unsorted sublist.
2. Swap it with the leftmost unsorted element.
3. Move the boundary of the sorted sublist one element to the right.
4. Repeat steps 1-3 until the entire array is sorted.

The time performance of selection sort is strictly **O(N^2)**.

## 2 - Bubble Sorting
Procedure:

1. Start at the beginning of the array. 
2. Compare each pair of adjacent elements. 
3. If the elements are in the wrong order, swap them. 
4. Move to the next pair of elements. 
5. Repeat steps 2-4 until no swaps are needed, indicating that the array is sorted. 

The time performance of bubble sort is strictly **O(N^2)**.

## 3 - Insertion Sorting
Procedure:
1. Start with the second element: Assume the first element of the array is already sorted. So, we start with the second 
element. 
2. Compare and insert: Compare the current element with the elements to its left in the sorted part of the array. Move 
the elements to the right until finding the correct position for the current element. 
3. Repeat: Repeat step 2 for each subsequent element in the unsorted part of the array until the entire array is sorted.

Insertion Sort has an average and worst-case time complexity of **O(n^2)**. However, its best-case time
complexity is O(n) when the input array is already sorted.

## Implementation Summary
1. The External Loop:
The external loop controls the iteration times, each of which represents an extension/update of sorted area. In the case,
we have length n array, then each iteration we increase the sorted area by 1 elements, beginning with comparing 2 elements.
Therefore, we need to `n-1` (=`(1+1*(n-2))`) times of external iterations.
2. The Internal Loop:
The internal loop aims to put the unsorted element to its sorted location in this external loop.


   

