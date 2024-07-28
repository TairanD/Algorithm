# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def iisPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        length = len(node_list)
        first_half = node_list[:length >> 1]
        if length % 2 == 0:
            # wrong version: reversed_second_half = node_list[length:length >> 1:-1]
            reversed_second_half = node_list[length:(length>>1)-1:-1]
        else:
            # wrong version: reversed_second_half = node_list[length:length >> 1 + 1:-1]
            reversed_second_half = node_list[length:length>>1:-1]
        return first_half == reversed_second_half

    def isPalindrome(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
"""
Note:
1. the relationship between the index & the length
"""


head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1))))))
print(Solution().isPalindrome(head))
