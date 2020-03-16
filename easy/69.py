class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)


if __name__ == '__main__':
    sol = Solution()
    output = sol.mySqrt(101)
    print(output)