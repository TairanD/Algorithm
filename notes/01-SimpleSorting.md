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