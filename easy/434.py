class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        if " " not in s:
            return 1
        segments = s.split(" ")
        while "" in segments:
            segments.remove("")
        return len(segments)


if __name__ == '__main__':
    sol = Solution()
    output = sol.countSegments("")
    print(output)