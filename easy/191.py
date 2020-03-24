class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n & 1
            n >>= 1
        return count


if __name__ == '__main__':
    sol = Solution()
    output = sol.hammingWeight(11111111111111111111111111111101)
    print(output)