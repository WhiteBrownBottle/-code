class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        inter = set(nums1) & set(nums2)
        ans = []
        for i in inter:
            ans + [i] * min(nums1.count(i), nums2.count(i))
        return ans
