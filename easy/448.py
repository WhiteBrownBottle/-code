class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        result = [*range(1, len(nums) + 1)]
        for n in nums:
            result[n - 1] = 0
        for i in range(len(result) - 1, -1, -1):
            if not result[i]:
                result.pop(i)
        return result


if __name__ == '__main__':
    sol = Solution()
    output = sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print(output)
