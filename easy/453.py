class Solution:
    def minMoves(self, nums: list) -> int:
        return sum(nums) - len(nums) * min(nums)