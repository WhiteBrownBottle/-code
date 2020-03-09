class Solution:
    def removeElement(self, nums: list, val: int) -> int:
            j = 0
            for i in range(0, len(nums)):
                if nums[i] != val:
                        nums[j] = nums[i]
                        j = j + 1
            return j


if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]
    output = sol.removeElement(nums, 0)
    print(nums)
    print(output)