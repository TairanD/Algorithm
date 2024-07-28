# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0
        idx = 1
        while l1:
            num1 += idx * l1.val
            idx *= 10
            l1 = l1.next
        idx = 1
        while l2:
            num2 += idx * l2.val
            idx *= 10
            l2 = l2.next
        sum = num1 + num2
        if sum == 0:
            return ListNode(0)
        dummy = ListNode()
        prev = dummy
        while sum > 0:
            cur = ListNode(sum % 10)
            prev.next = cur
            prev = cur
            sum = sum // 10
        return dummy.next
