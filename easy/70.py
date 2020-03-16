class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(3, n+1):
            temp = i1 + i2
            i1 = i2
            i2 = temp
        return temp






if __name__ == '__main__':
    sol = Solution()
    output = sol.climbStairs(4)
    print(output)


# 4
# 1111 22 211 121 112
# 5
# 11111 221 212 122