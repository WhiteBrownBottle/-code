class Solution:
    def constructRectangle(self, area: int) -> list:
        if area <= 1:
            return None
        res_list = []
        res_dict = {}
        half = int(area**0.5)
        for i in range(1, half+1):
            if area % i == 0:
                res_list.append([max(i, area // i), min(i, area // i)])
                res_dict[len(res_list)-1] = abs(i - area // i)
        index = 0
        for key, value in res_dict.items():
            if value == min(res_dict.values()):
                index = key
        return res_list[index]



if __name__ == '__main__':
    sol = Solution()
    output = sol.constructRectangle(100)
    print(output)
