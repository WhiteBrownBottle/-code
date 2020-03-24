class Solution1:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums.insert(0, nums.pop())
            k -= 1


class Solution2:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        count = n - k
        tmp = nums[:]
        for i in range(n):
            nums[i] = tmp[(i+count)%n]


class Solution3:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        count = n - k  #4
        tmp = nums[:]
        for i in range(n):
            nums[(i+count)%n] = tmp[i]
