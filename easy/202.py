class Solution:
    def isHappy(self, n: int) -> bool:
        ans_list = []
        flag = True
        while flag:
            ans = 0
            if n in ans_list:
                return False
            ans_list.append(n)
            while n > 0:
                ans += (n % 10) * (n % 10)
                n = n // 10
            if ans != 1:
                n = ans
            else:
                flag = False
                return True

if __name__ == '__main__':
    sol = Solution()
    output = sol.isHappy(37)
    print(output)


