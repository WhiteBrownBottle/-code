class Solution:
    def longestCommonPrefix(self, strs: list):
        if len(strs) == 0:
            return ""
        all_len = len(strs)
        min_len = len(strs[0])
        word = strs[0]
        flag = 1
        for i in range(0, all_len):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                word = strs[i]
        letter = [[] for i in range(min_len)]
        for i in range(0, min_len):
            for j in range(0, all_len):
                letter[i].append(strs[j][i])
        letter.append(['a','b','c'])
        for i in range(len(letter)):
            if len(set(letter[i])) != 1:
                if i == 0:
                    return ""
                else:
                    flag = i
                    return word[:flag]







if __name__ == '__main__':
    sol = Solution()
    output = sol.longestCommonPrefix(["aa", "aa"])
    print(output)
