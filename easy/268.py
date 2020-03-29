class Solution:
    def missingNumber(self, nums: list) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            else:
                return i
        return i + 1
