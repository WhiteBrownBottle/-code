class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1 or num <= 0:
            return False
        res = [1]
        mid = int(num ** 0.5)
        for i in range(2, mid + 1):
            if i in res:
                continue
            if num % i == 0:
                res.append(i)
                if i == num // i:
                    continue
                res.append(num // i)
        return sum(res) == num


if __name__ == '__main__':
    sol = Solution()
    output = sol.checkPerfectNumber(28)
    print(output)

