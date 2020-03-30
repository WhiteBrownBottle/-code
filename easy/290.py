class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern and not str:
            return True
        elif not pattern and str:
            return False
        elif pattern and not str:
            return False
        pattern_list = list(pattern)
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        pattern_dict = {}
        for i in range(len(pattern)):
            key = pattern_list[i]
            value = str_list[i]
            if key not in pattern_dict.keys():
                pattern_dict[key] = value
                continue
            if pattern_dict.get(key) != value:
                return False
        a = len(pattern_dict)
        b = len(set(pattern_dict.values()))
        return len(pattern_dict) == len(set(pattern_dict.values()))


if __name__ == '__main__':
    sol = Solution()
    output = sol.wordPattern("abba", "dog cat cat dog")
    print(output)



