# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        nums1 = nums[:mid]
        nums2 = nums[mid+1:]
        node.left = self.sortedArrayToBST(nums1)
        node.right = self.sortedArrayToBST(nums2)
        return node