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

Preorder, Inorder, & Postorder

## Breadth First Search

## Find the largest breadth

## Estimate if a binary tree a BST
Wrong Implementation by me:
```
public static boolean ifBST(Node root){
    if (root == null){
    return true;
    }

    if (root.left != null){
    if (root.left.value > root.value){
    return false;
    }
    }

    if (root.right != null){
    if (root.right.value > root.value){
    return false;
    }
    }

    return ifBST(root.left) && ifBST(root.right);
}
```
The above code can only guarantee the parent node and their children obey the rule of BST. Yet, a BST requires 
- the left subtree (all nodes in this subtree instead of only left child) of a node _n_ are less than the value of _n_
- the right subtree (all nodes in this subtree instead of only right child) of a node _n_ are greaterjk than the value of _n_