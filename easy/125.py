class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        value = 'abcdefghijklmnopqrstuvwxyz0123456789'
        value_list = list(value)
        s_list = list(s.lower())
        pure_s = []
        for i in range(len(s_list)):
            if s_list[i] in value_list:
                pure_s.append(s_list[i])
        length = len(pure_s)
        if length % 2 == 0:
            for i in range(length // 2):
                if pure_s[i] != pure_s[length-1-i]:
                    return False
        else:
            middle = length // 2
            for i in range(length // 2 + 1):
                if pure_s[middle-i] != pure_s[middle+i]:
                    return False
        return True





if __name__ == '__main__':
    sol = Solution()
    output = sol.isPalindrome("A man, a plan, a canal: Panama")
    print(output)
