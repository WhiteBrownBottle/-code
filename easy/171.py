class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x)-ord('A')+1
        return ans


if __name__ == '__main__':
    sol = Solution()
    output = sol.titleToNumber("ABC")
    print(output)