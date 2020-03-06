class Solution:
    def twoSum(self, nums: list, target: int):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target-nums[i]) in temp:
                j = temp.index(target-nums[i])
                break
        if j >= 0:
            return [j, i]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))