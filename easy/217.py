class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

