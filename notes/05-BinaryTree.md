# Binary Tree

### Note
Traversing a binary tree through recursion will follow this [rule](https://github.com/TairanD/Data-Struc-Algorithm-TA/blob/main/notes/04-tree-traversals.md#2).
Each function evoked will be store in a stack frame in the stack memory. The types of traversal (i.e. preorder, inorder, 
& postorder) are determined by the arrangement of the recursion function as the recursive function will wait the completion
of the currently executing stack frame, which means eventually, it will recover and continue to run. 

However, if traversing a binary tree using iteration, we will use stack ADT and add Node objects to the stack. In this 
case, any pop of node necessarily means we cannot go back to the node (unlike recursion). Therefore, leading to the 
seemingly different implementing strategy even though they both use stack.

## Traverse a Binary Tree using Iteration

### Preorder


### Inorder


### Postorder