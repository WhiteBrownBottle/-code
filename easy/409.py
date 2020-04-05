class Solution:
    def longestPalindrome(self, s: str) -> int:
        palindrome = {}
        s_list = list(s)
        for i in s_list:
            if i in palindrome.keys():
                palindrome[i] += 1
            else:
                palindrome[i] = 1
        sum = 0
        for key, value in palindrome.items():
            sum += value // 2 * 2
            if value % 2 == 1 and sum % 2 == 0:
                sum += 1
        return sum



if __name__ == '__main__':
    sol = Solution()
    output = sol.longestPalindrome("ababababa")
    print(output)

