class Solution:
    def reverseVowels(self, s: str) -> str:
        yuanyin_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = list(s)
        ys = [c for c in s_list if c in yuanyin_list]
        ys.reverse()
        index = 0
        for i in range(len(s_list)):
            if s_list[i] in yuanyin_list:
                s_list[i] = ys[index]
                index += 1
        return str(s_list)