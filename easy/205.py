class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        map_s = {}
        for i in range(len(s)):
            if s[i] in map_s.keys():
                if map_s[s[i]] != t[i]:
                    return False
            else:
                map_s[s[i]] = t[i]
        if len(map_s) != len(set(map_s.values())):
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    output = sol.isIsomorphic("ab", "cc")
    print(output)
