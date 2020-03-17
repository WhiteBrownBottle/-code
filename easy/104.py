# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth_l = 1
        depth_r = 1
        if root.left is not None:
            depth_l += self.maxDepth(root.left)
        if root.right is not None:
            depth_r += self.maxDepth(root.right)
        return max(depth_l, depth_r)
