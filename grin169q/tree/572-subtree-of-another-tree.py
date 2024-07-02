# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSame(self, r1, r2):
        if not r1 and not r2:
            return True
        elif not r1 or not r2:
            return False

        if r1.val == r2.val:
            return self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)
        else:
            return False

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        if not self.isSame(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return True