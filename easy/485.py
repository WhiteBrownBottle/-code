class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        if not nums or 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)
        cnt = 0
        res = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        res = max(res, cnt)
        return res


