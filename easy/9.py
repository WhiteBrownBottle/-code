class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        else:
            s = str(x)[::-1]
            if int(s) == x:
                return True
            else:
                return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(1231))