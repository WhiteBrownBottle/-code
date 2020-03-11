class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle:
            if needle not in haystack:
                return -1
            else:
                flag = 0
                haystack_list = list(haystack)
                needle_list = list(needle)
                for i in range(0, len(haystack)):
                        for j in range(0, len(needle_list)):
                            if haystack[i+j] == needle_list[j]:
                                if j == len(needle_list) - 1:
                                    flag = 1
                                else:
                                    continue
                            else:
                                break
                        if flag:
                            return i
        else:
            return 0

if __name__ == '__main__':
    sol = Solution()
    output = sol.strStr("hello", "ll")
    print(output)