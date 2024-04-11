package code;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Stack;

public class Code04 {
    public static class Node<V extends Comparable<V>>{
        V value;
        public Node<V> next;

        public Node(V v){this.value = v;};
    }

    public static <V extends Comparable<V>> Node<V> reverseList(Node<V> head){
        // initialize current head node of the list
        Node<V> currentHead = head;
        // for each node after head, I'd like to swap it with current head node of the slinked list
        while (head.next!=null){
            // swap originalHead.next to the currentHead
            Node<V> next = head.next;
            head.next = next.next;
            next.next = currentHead;
            currentHead = next;

            /** There is a very common-used technique I'd like to point it out:
             *  To change sth. (like a particular code in the linked list),
             *  we need to store it firstly into another variable to prevent losing its value (if we still need to access to it),
             *  then assigning another variable to this one.
             *
             *  In this case, we store head.next to variable next so that we can perform further operations on it (next.next = currentHead;),
             *  and use it (currentHead = next;) again.
             *  **/
        }
        return currentHead;
    }

    public static <V extends Comparable<V>> Node<V> reverseList2(Node<V> head){
        Node<V> currentHead = head;
        Node<V> next = head.next;
        while (next!=null){
            head.next = next.next;
            next.next = currentHead;
            currentHead = next;
            next = head.next;
        }
        return currentHead;
    }

    public static <V extends Comparable<V>> void printLinkedList(Node<V> head) {
        System.out.print("Linked List: ");
        while (head != null) {
            System.out.print(head.value + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static class DoubleNode<V>{
        public V value;
        public DoubleNode<V> last;
        public DoubleNode<V> next;
        public DoubleNode(V v) {
            this.value = v;
        }
    }

    public static <V> DoubleNode<V> reverseList(DoubleNode<V> head){
        DoubleNode<V> currentHead = head;
        while (head.next!=null){
            // swap currentHead with the next node of the original head
            DoubleNode<V> next = head.next;
            head.next = next.next;
            if (next.next!=null)
                next.next.last = head;
            next.last = null;
            next.next = currentHead;
            currentHead.last = next;
            currentHead = next;
        }

        return currentHead;
    }


    public static <V> void printDoubleLinkedList(DoubleNode<V> head) {
        System.out.print("Double Linked List: ");
        DoubleNode<V> end = null;
        while (head != null) {
            System.out.print(head.value + " ");
            end = head;
            head = head.next;
        }
        System.out.print("| ");
        while (end != null) {
            System.out.print(end.value + " ");
            end = end.last;
        }
        System.out.println();
    }

    public static <V extends Comparable<V>> void printSharedPart(Node<V> list1, Node<V> list2){
        // list1 & list2 respectively represents the head node of list1 & list2, which are both ordered list
        ArrayList<Node<V>> share = new ArrayList<>();
        Node<V> p1 = list1;
        Node<V> p2 = list2;
        while (p1!=null && p2!=null){
            int result = p1.value.compareTo(p2.value);
            if (result == 0){
                share.add(p1);
                p1 = p1.next;
                p2 = p2.next;
            }else if (result<0){
                p1 = p1.next;
            }else {
                p2 = p2.next;
            }
        }
        for (Node<V> node: share){
            System.out.println("shared value: " + node.value);
        }
    }

    public static <V extends Comparable<V>> boolean ifPalindrome(Node<V> head){
        if (head == null){
            return false;
        }
        Stack<V> stack = new Stack<>();
        Node<V> slowerPointer = head;
        Node<V> fasterPointer = head;

        // I want the slower pointer be the middle node of the list
        // and when the length of the list is even
        while (true){
            // if slowerPointer = null, meaning that the list has only a head.
            if (slowerPointer.next==null){
                return true;
            }

            // (fasterPointer.next == null) means that the length of the list is odd
            // (because we start at head and jump two pace once a time for faster pointer)
            // and at this time, slowerPointer is at the middle location!
            if (fasterPointer.next == null){
                break;
                // (fasterPointer.next.next == null && fasterPointer.next != null) means the length of the list is even
                // and at the point, slowerPointer locates at the last node of the middle point of the list
                // so if I want it to be the next node of the middle point of the list, I need to 'next' it
            } else if (fasterPointer.next.next == null) {
                slowerPointer = slowerPointer.next;
                break;
            } else {
                slowerPointer = slowerPointer.next;
                fasterPointer = fasterPointer.next.next;
            }
        }
        while (slowerPointer != null){
            stack.add(slowerPointer.value);
            slowerPointer = slowerPointer.next;
        }
        Node<V> firstPart = head;
        while (firstPart.value.compareTo(stack.pop())==0){
            if (stack.empty()){
                return true;
            }
            firstPart = firstPart.next;
        }
        return false;
    }

    public static <V extends Comparable<V>> boolean ifPalindrome2(Node<V> head){
        if (head == null){
            return false;
        }
        Node<V> slowerPointer = head;
        Node<V> fasterPointer = head;

        // I want the slower pointer be the middle node of the list
        // and when the length of the list is even
        while (true){
            // if slowerPointer = null, meaning that the list has only a head.
            if (slowerPointer.next==null){
                return true;
            }

            // (fasterPointer.next == null) means that the length of the list is odd
            // (because we start at head and jump two pace once a time for faster pointer)
            // and at this time, slowerPointer is at the middle location!
            if (fasterPointer.next == null){
                break;
                // (fasterPointer.next.next == null && fasterPointer.next != null) means the length of the list is even
                // and at the point, slowerPointer locates at the last node of the middle point of the list
                // so if I want it to be the next node of the middle point of the list, I need to 'next' it
            } else if (fasterPointer.next.next == null) {
                slowerPointer = slowerPointer.next;
                break;
            } else {
                slowerPointer = slowerPointer.next;
                fasterPointer = fasterPointer.next.next;
            }
        }
        // in this loop, I need to reverse the right part of the list
        Node<V> reversedRightHead = reverseList(slowerPointer);
        /** I do not want to change the left side of the list, but at the same time, I want to iterate the list.
         *  Therefore, I need a variable that I can change (reassign) to visit other nodes in the list, meanwhile, it should
         *  contain information of the head node, which I do not want to change.
         *  ->
         *  I need to create a new variable to remember head object.
         *  In this way, I can access to head information and can reassign this temp variable without changing to the original list.
         *  In this case, I do not want to change head (because if I do so, we will lose the original head FOREVER), and I need to
         *  use information of head. Thus, I create a variable to remember head, and after access to data I need, I reassign the variable.
         * **/
        Node<V> temp = head;
        Node<V> temp2 = reversedRightHead;
        while (temp2!=null){
            if (temp.value!= temp2.value){
                reverseList(reversedRightHead);
                return false;
            }
            temp2 = temp2.next;
            temp = temp.next;
        }
        reverseList(reversedRightHead);
        return true;
    }

    public static <V extends Comparable<V>> void sort(Node<V> head){
        // I need to create 6 pointers (nodes) to trace the shared part
        Node<V> smallHead = new Node<>(null);
        Node<V> smallTail = new Node<>(null);
        Node<V> equalHead = new Node<>(null);
        Node<V> equalTail = new Node<>(null);
        Node<V> largerHead = new Node<>(null);
        Node<V> largerTail = new Node<>(null);
    }

    public static void main(String[] args) {
        Node<Integer> head1 = new Node<>(1);
        head1.next = new Node<>(2);
        head1.next.next = new Node<>(3);
        head1.next.next.next = new Node<>(4);
        head1.next.next.next.next = new Node<>(5);
        printLinkedList(head1);
        head1 = reverseList2(head1);
        printLinkedList(head1);

        DoubleNode<Integer> head2 = new DoubleNode<>(1);
        head2.next = new DoubleNode<>(2);
        head2.next.last = head2;
        head2.next.next = new DoubleNode<>(3);
        head2.next.next.last = head2.next;
        head2.next.next.next = new DoubleNode<>(4);
        head2.next.next.next.last = head2.next.next;
        printDoubleLinkedList(head2);
        printDoubleLinkedList(reverseList(head2));

        Node<Integer> head3 = new Node<>(4);
        head3.next = new Node<>(5);
        head3.next.next = new Node<>(6);
        head3.next.next.next = new Node<>(7);

        printLinkedList(head1);
        head1 = reverseList(head1);
        printSharedPart(head1, head3);
        printLinkedList(head1);


        Node<Integer> head4 = new Node<>(4);
        head4.next = new Node<>(5);
        head4.next.next = new Node<>(6);
        head4.next.next.next = new Node<>(5);
        head4.next.next.next.next = new Node<>(4);

        System.out.println(ifPalindrome2(head1));
        System.out.println(ifPalindrome2(head4));
        printLinkedList(head4);
    }
}