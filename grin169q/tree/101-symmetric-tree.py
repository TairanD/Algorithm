# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return

        root.right, root.left = root.left, root.right

        self.invertTree(root.left)
        self.invertTree(root.right)

    def ifSame(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        if root1.val == root2.val:
            return self.ifSame(root1.left, root2.left) and self.ifSame(root1.right, root2.right)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.invertTree(root.right)
        return self.ifSame(root.left, root.right)
