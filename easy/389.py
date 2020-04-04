class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_list = list(s)
        t_list = list(t)
        for i in s_list:
            t_list.remove(i)
        return t_list[0]


if __name__ == '__main__':
    sol = Solution()
    output = sol.findTheDifference("abcde", "baccde")
    print(output)

