class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        if not nums or k < 0:
            return 0
        if k == 0:
            return len(set([i for i in nums if nums.count(i)>=2]))
        ans = 0
        d = set()
        for num in nums:
            residual1 = num - k
            residual2 = num + k
            if num not in d:
                if residual1 in d:
                    ans += 1
                if residual2 in d:
                    ans += 1
            d.add(num)
        return ans


if __name__ == '__main__':
    sol = Solution()
    ouput = sol.findPairs([1, 2, 3, 4, 5], 2)
    print(ouput)

