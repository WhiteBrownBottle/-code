class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) < 2:
            return 0
        else:
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i]-prices[i-1]
            return res

if __name__ == '__main__':
    sol = Solution()
    output = sol.maxProfit([7,1,5,3,6,4])
    print(output)

