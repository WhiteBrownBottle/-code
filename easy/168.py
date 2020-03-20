# 26进制思维
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            res = chr(n % 26 + 65) + res
            n = n // 26
        return res



if __name__ == '__main__':
    sol = Solution()
    output = sol.convertToTitle(34234)
    print(output)
