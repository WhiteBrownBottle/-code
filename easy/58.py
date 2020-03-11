class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        s_list = s.split(' ')
        if s_list == ['']:
            return 0
        for i in s_list:
            if i == '':
                s_list.remove(i)
        return len(s_list[-1])


if __name__ == '__main__':
    sol = Solution()
    output = sol.lengthOfLastWord("   ")
    print(output)