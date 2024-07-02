# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def cal_height(self, head):
        if not head:
            return 0

        left_height = self.cal_height(head.left)
        right_height = self.cal_height(head.right)

        if left_height == 0 and right_height == 0:
            return 1
        else:
            return left_height + 1 if left_height > right_height else right_height + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if left and right:
            left_height = self.cal_height(root.left)
            right_height = self.cal_height(root.right)
            if abs(left_height - right_height) > 1:
                return False
            else:
                return True
        else:
            return False

    # Implementation above does not utilize the full power of the recursive function (cal_depth here)
    def cal_height_improved(self, head):
        if not head:
            return 0

        left_height = self.cal_height(head.left)
        right_height = self.cal_height(head.right)

        if left_height == 0 and right_height == 0:
            return 1
        elif abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
            return -1
        else:
            return left_height + 1 if left_height > right_height else right_height + 1

    def isBalanced_improved(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.cal_height(root) >= 0
