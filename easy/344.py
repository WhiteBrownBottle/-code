class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        s_len = len(s)
        if s_len == 1:
            return s
        if s_len % 2 == 0:
            for i in range(0, s_len, 1):
                j = s_len - 1 - i
                tmp = s[j]
                s[j] = s[i]
                s[i] = tmp
                if j - i == 1:
                    break
        else:
            for i in range(0, s_len, 1):
                j = s_len-1-i
                if j == i:
                    break
                else:
                    tmp = s[j]
                    s[j] = s[i]
                    s[i] = tmp


if __name__ == '__main__':
    s = ["H","a","n","n","a","h"]
    sol = Solution()
    sol.reverseString(s)
    print(s)

