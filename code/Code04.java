package code;

public class Code04 {
    public static class Node<V>{
        V value;
        public Node<V> next;

        public Node(V v){this.value = v;};
    }

    public static <V> Node<V> reverseList(Node<V> head){
        // initialize current head node of the list
        Node<V> currentHead = head;
        // for each node after head, i'd like to swap it with current head node of the slinked list
        while (head.next!=null){
            // swap originalHead.next to the currentHead
            Node<V> next = head.next;
            head.next = next.next;
            next.next = currentHead;
            currentHead = next;
        }
        return currentHead;
    }

    public static <V> Node<V> reverseList2(Node<V> head){
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

    public static <V> void printLinkedList(Node<V> head) {
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

    public static void printDoubleLinkedList(DoubleNode head) {
        System.out.print("Double Linked List: ");
        DoubleNode end = null;
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

    }
}
