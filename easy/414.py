class Solution:
    def thirdMax(self, nums: list) -> int:
        max1, max2, max3 = [-float("inf")] * 3
        for i in nums:
            if max1 == i or max2 == i or max3 == i:
                continue
            elif i > max1:
                max1, max2, max3 = i, max1, max2
            elif i > max2:
                max2, max3 = i, max2
            elif i > max3:
                max3 = i
        return max1 if max3 == -float("inf") else max3
