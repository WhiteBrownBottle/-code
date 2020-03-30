# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n + 1  # 利用左闭右开的特性，所以右端点加1，这样的好处是当while loop终止时，right、mid、left三者取值相同，不用思考需要返回哪一个，返回哪一个都是正确的
        while (left < right):
            mid = left + (right - left) // 2
            # 当前版本为正确，则替换mid
            if (isBadVersion(mid) == False):
                left = mid + 1
            else:
                right = mid
        return right



if __name__ == '__main__':
    sol = Solution()
    output = sol.firstBadVersion(100)
    print(output)


