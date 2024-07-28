# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        res = ListNode(0, head)
        prev = res
        while head and head.next:
            next_node = head.next.next
            head.next.next = head
            prev.next = head.next
            prev = head.next
            head.next = next_node
            head = next_node
        return res.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(Solution().swapPairs(head).val)
print(Solution().swapPairs(head.next).val)
print(Solution().swapPairs(head.next).val)