class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) <= 2:
            return len(nums)
        else:
            j = 0
            for i in range(1, len(nums)):
                if nums[j] != nums[i]:
                    j = j+1
                    nums[j] = nums[i]
            return j+1


if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,2,3,3,4,5]
    output = sol.removeDuplicates(nums)
    print(nums)