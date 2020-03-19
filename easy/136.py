class Solution:
    def singleNumber(self, nums: list) -> int:
        nums.sort()
        nums.append(0)
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                return nums[i]
