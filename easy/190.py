#这题真不会
class Solution:
    def reverseBits(self, n: int) -> int:
        k, res = 0, 0
        while k < 32:
            res <<= 1
            res = res | (n & 1)
            n >>= 1
            k += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    output = sol.reverseBits(11111111111111111111111111111101)
    print(output)