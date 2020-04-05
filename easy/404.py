# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum = 0
        def calLeftLeaves(node : TreeNode):
            if node.left:
                if node.left.left or node.left.right:
                    calLeftLeaves(node.left)
                else:
                    self.sum += node.left.val
                    calLeftLeaves(node.left)
            if node.right:
                calLeftLeaves(node.right)
        calLeftLeaves(root)
        return self.sum


