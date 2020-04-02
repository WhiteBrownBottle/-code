class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        s_list = list(s)
        word = {}
        for i in s_list:
            if i not in word.keys():
                word[i] = 1
            else:
                word[i] += 1

        for i in s_list:
            if word[i] == 1:
                return s_list.index(i)
        return -1






