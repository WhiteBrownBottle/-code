class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        def get_bin_nums(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            num = num // 2
            return get_bin_nums(num) + 1
        bin_nums = get_bin_nums(num)
        bin_max = 2 ** bin_nums - 1
        return bin_max - num


if __name__ == '__main__':
    sol = Solution()
    output = sol.findComplement(5)
    print(output)