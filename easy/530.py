# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def preorder(root: TreeNode):
            if not root:
                return []
            else:
                return preorder(root.left) + [root.val] + preorder(root.right)

        target = preorder(root)
        n = len(target)
        res = 10000
        for i in range(n - 1):
            res = min(target[i + 1] - target[i], res)
        return res