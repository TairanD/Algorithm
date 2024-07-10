# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res, level = [], [root]
        # 在Python中，如果将一个包含None的列表传递给if语句，条件会被视为True，因为列表本身是非空的，即使它包含的是None。只有当列表为空时，if条件才会被视为False。
        while root and level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        return res


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().levelOrder(root=root))
