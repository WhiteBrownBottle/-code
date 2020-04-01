class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        res = [a for a in nums1 if a in nums2]
        res = list(set(res))
