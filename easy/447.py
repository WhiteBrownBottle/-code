class Solution:
    def numberOfBoomerangs(self, points: list) -> int:
        result = 0
        for i in points:
            dis = {}
            for j in points:
                distance = (i[0]-j[0])**2 + (i[1]-j[1])**2
                if distance not in dis:
                    dis[distance] = 1
                else:
                    dis[distance] += 1
            for val in dis.values():
                if val >= 2:
                    result += val * (val - 1)
        return result
