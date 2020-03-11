class Solution:
    def maxSubArray(self, nums: list) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums[i])


if __name__ == '__main__':
    sol =Solution()
    output = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(output)