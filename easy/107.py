# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list]:
        tree = []

        def returnSonTree(node:TreeNode, depth):
            if not node: return tree
            if depth == len(tree):
                tree.append([])
            tree[depth].append(node.val)
            returnSonTree(node.left, depth+1)
            returnSonTree(node.right, depth+1)
        returnSonTree(root, 0)
        return tree[::-1]