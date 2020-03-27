class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        if len(nums)<= 0 or k == 0:
            return False
        hash_x = dict()
        for i in range(len(nums)):
            if hash_x.get(nums[i]) is not None and (i - hash_x.get(nums[i])) <= k:
                return True
            hash_x[nums[i]] = i
        return False



