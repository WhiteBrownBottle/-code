# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None

        def findRoot(node: TreeNode, p : TreeNode, q : TreeNode):
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node
            elif p.val < node.val and q.val < node.val:
                return findRoot(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                return findRoot(node.right, p, q)
        return findRoot(root, p, q)
