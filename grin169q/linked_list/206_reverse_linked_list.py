# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        i = len(node_list) - 1
        while i != 0:
            node_list[i].next = node_list[i - 1]
            i -= 1
        node_list[0].next = None

        return node_list[-1]