# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def process(self, head, diction):
        if not head:
            diction[head] = None
            return 0

        left_height = self.process(head.left, diction)
        right_height = self.process(head.right, diction)

        diction[head] = left_height + right_height
        return left_height + 1 if left_height > right_height else right_height + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth_sums = {}
        self.process(root, depth_sums)
        max = 0
        for depth_sum in depth_sums:
            if depth_sums[depth_sum] > max:
                max = depth_sums[depth_sum]
        return max