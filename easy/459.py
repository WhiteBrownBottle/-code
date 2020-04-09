class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        index = 1
        while index < length // 2 + 1:
            if s[index] == s[0]:
                templow = 0
                temphigh = index
                count = 0
                while temphigh < length:
                    if s[templow] == s[temphigh]:
                        temphigh += 1
                        templow += 1
                        count += 1
                    else:
                        break
                if temphigh == length and count % index == 0:
                    return True
            index += 1
        return False

class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1: len(s)*2 -1].find(s) != -1

if __name__ == '__main__':
    sol = Solution()
    output = sol.repeatedSubstringPattern("abcabcabcabc")
    print(output)