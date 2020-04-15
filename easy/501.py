# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> list:
        if not root:
            return []
        queue = [root]
        tree_dict = {}
        while queue:
            node = queue.pop(0)
            if node.val not in tree_dict:
                tree_dict[node.val] = 1
            else:
                tree_dict[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res = []
        m = max(tree_dict.values())
        for key, value in tree_dict.items():
            if value == m:
                res.append(key)
        return res


