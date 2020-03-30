class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        old_len = len(nums)
        nums[:] = list(filter(lambda x: x != 0, nums))
        new_len = len(nums)
        for i in range(old_len - new_len):
            nums.append(0)


if __name__ == '__main__':
    test = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.moveZeroes(test)
    print(test)

