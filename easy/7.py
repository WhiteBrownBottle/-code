class Solution:
    def reverse(self, x: int):
        s = str(x)[::-1].rstrip('-')
        if int(s) < 2**31:
            if x > 0:
                return int(s)
            else:
                return  0 - int(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(123))