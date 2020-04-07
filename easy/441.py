class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n or n < 0:
            return 0
        coin = {}
        tmp = 0
        i = 0
        while tmp <= n:
            tmp += i
            coin[i] = tmp
            i += 1
        for key, value in coin.items():
            if value > n:
                return key - 1
            elif value == n:
                return key

if __name__ == '__main__':
    sol = Solution()
    output = sol.arrangeCoins(1804289383)
    print(output)



