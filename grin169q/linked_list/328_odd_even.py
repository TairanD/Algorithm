# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = ListNode(0, head)
        odd_ptr = odd_head
        even_head = ListNode(0, head.next)
        even_ptr = even_head
        idx = 1
        while head:
            if idx % 2 == 1:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = head
                even_ptr = even_ptr.next
            idx += 1
            head = head.next
        even_ptr.next = None  # ensures the even list is properly terminated and doesn't inadvertently link back to any nodes that might follow it in memory
        odd_ptr.next = even_head.next
        return odd_head.next
