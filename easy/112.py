# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        all = []
        if not root:
            return False
        def returnRoadSum(node, num):
            num += node.val
            if not node.left and not node.right:
                all.append(num)
            else:
                if node.left:
                    returnRoadSum(node.left, num)
                if node.right:
                    returnRoadSum(node.right, num)
        returnRoadSum(root, 0)
        if sum in all:
            return True
        else:
            return False


