# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
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
"""
Note:
1. the relationship between the index & the length
"""


head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(Solution().isPalindrome(head))
