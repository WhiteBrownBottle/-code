class Solution:
    def majorityElement(self, nums: list) -> int:
        nums_set = set(nums)
        nums_dict = {}
        for i in nums_set:
            nums_dict[i] = 0
        for i in nums:
            if i in nums_dict.keys():
                nums_dict[i] += 1
        for key, value in nums_dict.items():
            if value == max(nums_dict.values()):
                return key



if __name__ == '__main__':
    sol = Solution()
    output = sol.majorityElement([2,2,1,1,1,2,2])
    print(output)