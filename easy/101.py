# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            def check(node1, node2):
                if node1 is None and node2 is None:
                    return True
                if node1 is None or node2 is None:
                    return False
                if node1.val == node2.val:
                    return check(node1.left, node2.right) and check(node1.right, node2.left)
                return False
            return check(root.left, root.right)


