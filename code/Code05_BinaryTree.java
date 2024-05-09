package code;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Code05_BinaryTree {
    static class Node{
        int value;
        Node left;
        Node right;

        public Node(int data) {
            this.value = data;
        }
    }


    // to traverse a tree using iteration in preorder, we need to use stack data structure
    // and add node in order of parent, right, & left
    public void preOrderIter(Node root){
        if (root==null){
            return;
        }
        Stack<Node> stack = new Stack<>();
        // initialize the stack
        stack.add(root);
        while(!stack.isEmpty()){
            root = stack.pop();
            // do some perform to the node n here
            System.out.println(root.value);
            // Add the right firstly, then the left. Why?
            // Due to the LIFO property of stack, the node enter lately will be popped firstly
            if (root.right!=null){
                stack.add(root.right);
            }
            if (root.left!=null){
                stack.add(root.left);
            }
        }
    }

    public void inOrderIter(Node root){
        if (root==null){
            System.out.println("Input a valid value");
            return;
        }

        Stack<Node> stack = new Stack<>();
        // initialize the stack
        stack.add(root);
        while (!stack.isEmpty()){
            if (root!=null){
                root = root.left;
                stack.add(root);
            }else{
                root = stack.pop();
                // do some perform to the node root here
                System.out.println(root.value);
                root = root.right;
            }
        }
    }


    public void postOrderIter(Node root){
        if (root==null){
            return;
        }

        Stack<Node> stack = new Stack<>();
        // initialize stack
        stack.add(root);
        Stack<Node> stack2 = new Stack<>();
        while (!stack.isEmpty()){
            root = stack.pop();
            // perform some operations after pop
            stack2.add(root);
            if (root.left!=null){
                stack.add(root.left);
            }
            if (root.right!=null){
                stack.add(root.right);
            }
        }
        while(!stack2.isEmpty()){
            root = stack2.pop();
            // perform some operations here
            System.out.println(root.value);
        }
    }


    public void breadthFirst(Node root){
        if (root==null){
            return;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()){
            root = queue.poll();
            // perform operations here
            System.out.println(root.value);
            if (root.left!=null){
                queue.add(root.left);
            }
            if (root.right!=null){
                queue.add(root.right);
            }
        }
    }


    public static int maxLevelNodes(Node root){
        if (root==null){
            return -1;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        HashMap<Node, Integer> map = new HashMap<>();
        int curLevel = 0;
        int curLevelNodeNumber = 1;
        int max = Integer.MIN_VALUE;
        map.put(root, 1);
        while (!queue.isEmpty()){
            root = queue.poll();
            // perform operations here
            if (curLevel == map.get(root)){
                curLevelNodeNumber++;
            }else {
                max = Math.max(max, curLevelNodeNumber);
                curLevelNodeNumber = 1;
                curLevel++;
            }


            if (root.left!=null){
                queue.add(root.left);
                map.put(root.left, map.get(root) + 1);
            }
            if (root.right!=null){
                queue.add(root.right);
                map.put(root.right, map.get(root) + 1);
            }
        }

        return Math.max(max, curLevelNodeNumber);
    }

    public static int getMaxWidth(Node head) {
        if (head == null) {
            return 0;
        }
        int maxWidth = 0;
        int curWidth = 0;
        int curLevel = 0;
        HashMap<Node, Integer> levelMap = new HashMap<>();
        levelMap.put(head, 1);
        LinkedList<Node> queue = new LinkedList<>();
        queue.add(head);
        Node node = null;
        Node left = null;
        Node right = null;
        while (!queue.isEmpty()) {
            node = queue.poll();
            left = node.left;
            right = node.right;
            if (left != null) {
                levelMap.put(left, levelMap.get(node) + 1);
                queue.add(left);
            }
            if (right != null) {
                levelMap.put(right, levelMap.get(node) + 1);
                queue.add(right);
            }
            if (levelMap.get(node) > curLevel) {
                curWidth = 0;
                curLevel = levelMap.get(node);
            } else {
                curWidth++;
            }
            maxWidth = Math.max(maxWidth, curWidth);
        }
        return maxWidth;
    }


    public static boolean ifBST(Node root){
        if (root==null){
            return true;
        }

        boolean ifLeft = ifBST(root.left);

        // do operations here - inorder


        boolean ifRight = ifBST(root.right);

        return true;
    }


    public static void main(String[] args) {
        Node head = new Node(1);
        head.left = new Node(-222222222);
        head.right = new Node(3);
        head.left.left = new Node(Integer.MIN_VALUE);
        head.left.right = new Node(Integer.MIN_VALUE);
        head.right.left = new Node(55555555);
        head.right.left.left = new Node(55555555);
        head.right.left.right = new Node(55555555);
        head.right.right = new Node(66);
        head.right.right.right = new Node(66);
        head.right.right.left = new Node(66);
        head.left.left.right = new Node(777);

        System.out.println(maxLevelNodes(head));
    }
}

// x 有右树 -> x.right.left.left....
// x 无右树 ->
//      1. x为其父节点的右节点
//      2. x为其父节点的左节点: 就是x.parent