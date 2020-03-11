class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            new_nums = []
            if target < min(nums):
                new_nums.append(target)
                new_nums.extend(nums)
            elif target > max(nums):
                new_nums = nums
                nums.append(target)
            else:
                for i in range(0, len(nums)):
                    if nums[i] < target and nums[i + 1] > target:
                        new_nums = nums[:i + 1]
                        new_nums.append(target)
                        new_nums.extend(nums[i + 1:])
            return new_nums.index(target)


if __name__ == '__main__':
    sol = Solution()
    output = sol.searchInsert([1, 3, 4, 6], 0)
    print(output)