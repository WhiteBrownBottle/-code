import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        i = math.log10(n) / math.log10(3)
        return i == int(i)


if __name__ == '__main__':
    sol = Solution()
    output = sol.isPowerOfThree(27)
    print(output)