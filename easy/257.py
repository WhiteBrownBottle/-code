# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        if not root:
            return []
        footprint = []

        def returnFootPrint(node: TreeNode, print: str):
            if not node.left and not node.right:
                footprint.append(print)
            tmp_left = print
            tmp_right = print
            if node.left:
                tmp_left += "->" + str(node.left.val)
                returnFootPrint(node.left, tmp_left)
            if node.right:
                tmp_right += "->" + str(node.right.val)
                returnFootPrint(node.right, tmp_right)

        returnFootPrint(root, str(root.val))
        return footprint
