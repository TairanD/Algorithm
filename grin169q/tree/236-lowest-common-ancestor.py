# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def process(self, cur, father, dic_target):
        if not cur:
            return
        dic_target[cur] = father
        self.process(cur.left, cur, dic_target)
        self.process(cur.right, cur, dic_target)


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root:
            return p
        elif q == root:
            return q

        diction = {}
        self.process(root, root, diction)

        set_p = {p, root}
        while diction[p] != root:
            set_p.add(diction[p])
            p = diction[p]
        if q not in set_p:
            while diction[q] not in set_p:
                q = diction[q]
            return diction[q]
        else:
            return q