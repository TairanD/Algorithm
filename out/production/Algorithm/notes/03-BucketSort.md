# Bucket Sort

## 1 - Heap
#### Before Heap: Priority Queue
A priority queue is an abstract data type similar to a regular queue (FIFO) or stack data structure, in which each
element additionally has a '**priority**' associated with it. In a priority queue, elements with higher priority is served
before elements with lower priority. 

In daily life, we would assign different priorities to tasks, start working on the task with the highest priority and 
then proceed to the task with the second-highest priority. This is an example of a Priority Queue. Heap can be considered as a way
to implement a Priority Queue. There are multiple ways to implement a Priority Queue, such as array and linked list.
However, these implementations only guarantee `O(1)` time complexity for either insertion or deletion, while the other
operation will have a time complexity of `O(N)`. On the other hand, implementing the priority queue with Heap will allow
both insertion and deletion to have a time complexity of `O(log N)`.

#### Definition: 
A Heap is a **complete binary tree** data structure that satisfies the **heap property**. 

#### Types: 
Based on different heap properties, we have:
1. Max Heap: The root node contains the maximum value, and the values decrease as you move down the tree.
2. Min Heap: The root node contains the minimum value, and the values increase as you move down the tree.

#### Operations: 
1. Insertion of an element into the Heap has a time complexity of `O(log N)`.
2. Deletion of an element from the Heap has a time complexity of `O(log N)`.
3. The maximum/minimum value in the Heap can be obtained with `O(1)` time complexity.

## 2 - Heap Sort
#### Parent Children Relationship
If we use an array to represent the complete binary tree, and store the root node at index 1, we have the following relationship:
1. index of the parent node of any child node is `index of the node / 2`
2. index of the left child node is `index of the parent node * 2`
3. index of the right child node is `index of the parent node * 2 + 1`

If we use an array to represent the complete binary tree, and store the root node at index 0, we have the following relationship:
1. index of the parent node of any child node is `index of the node - 1 / 2`
2. index of the left child node is `index of the parent node * 2 + 1`
3. index of the right child node is `index of the parent node * 2 + 2`



