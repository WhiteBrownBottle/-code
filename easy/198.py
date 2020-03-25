class Solution:
    def rob(self, nums: list) -> int:
        if len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        now = 0
        last = 0
        for i in range(len(nums)):
            tmp = last
            last = now
            now = max(tmp + nums[i], now)
        return now

if __name__ == '__main__':
    sol = Solution()
    output = sol.rob([1,2,3,1])
    print(output)




