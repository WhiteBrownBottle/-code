# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.returnDepth(root) != -1
    def returnDepth(self, node):
        if not node:
            return 0
        left = self.returnDepth(node.left)
        if left == -1:
            return -1
        right = self.returnDepth(node.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1
