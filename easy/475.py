class Solution:
    def findRadius(self, houses: list, heaters: list) -> int:
        res = []
        # 排序
        houses.sort()
        heaters.sort()
        for c in houses:
            # 二分查找，在heaters中寻找与房屋 c 最近的加热器
            left = 0
            right = len(heaters) - 1
            while left < right:
                mid = (left + right) >> 1
                if heaters[mid] < c:
                    left = mid + 1
                else:
                    right = mid
            # 若找到的值等于 c ，则说明 c 房屋处放有一个加热器，c 房屋到加热器的最短距离为 0
            if heaters[left] == c:
                res.append(0)
            # 若该加热器的坐标值小于 c ，说明该加热器的坐标与 c 之间没有别的加热器
            elif heaters[left] < c:
                res.append(c - heaters[left])
            # 若该加热器的坐标值大于 c 并且left不等于 0 ，说明 c 介于left和left-1之间，
            # 房屋到加热器的最短距离就是left和left - 1处加热器与 c 差值的最小值
            elif left:
                res.append(min(heaters[left] - c, c - heaters[left - 1]))
            else:
                res.append(heaters[left] - c)
        return max(res)


if __name__ == '__main__':
    sol = Solution()
    output = sol.findRadius([1,2,3,5,15], [2,30])
    print(output)

