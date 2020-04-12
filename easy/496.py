class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        hashmap = {}

        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)
        return [hashmap.get(x, -1) for x in nums1]