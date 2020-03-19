class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) <=1:
            return 0
        min_num = prices[0]
        max_num = 0
        for i in range(0, len(prices)):
            max_num = max(max_num, prices[i]-min_num)
            min_num = min(min_num, prices[i])
        return max_num


if __name__ == '__main__':
    sol = Solution()
    output = sol.maxProfit([7,1,5,3,6,4])
    print(output)
