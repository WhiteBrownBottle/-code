class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote and not magazine:
            return True
        elif not magazine:
            return False
        ransomNote_list = list(ransomNote)
        magazine_list = list(magazine)
        for i in ransomNote_list:
            if i in magazine_list:
                magazine_list.remove(i)
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    output = sol.canConstruct("aa", "ab")
    print(output)