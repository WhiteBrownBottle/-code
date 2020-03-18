# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth_l = []
        depth_r = []

        def returnDepth(node, depth, lor):
            if not node.left and not node.right:
                if lor == 'l':
                    depth_l.append(depth+1)
                elif lor == 'r':
                    depth_r.append(depth+1)
            else:
                depth += 1
                if node.left:
                    returnDepth(node.left, depth, lor)
                if node.right:
                    returnDepth(node.right, depth, lor)
        if root.left:
            returnDepth(root.left, 1, 'l')
        if root.right:
            returnDepth(root.right, 1, 'r')
        if not root.left and not root.right:
            return 1
        return min(depth_l + depth_r)