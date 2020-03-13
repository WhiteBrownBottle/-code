class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ''
        res = []
        a = list(a)
        b = list(b)
        for i in range(max(len(a), len(b))+1):
            res.append("0")
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b.insert(0, '0')
        else:
            for i in range(len(b)-len(a)):
                a.insert(0, '0')
        for i in range(len(a)-1, -1, -1):
            if int(a[i]) + int(b[i]) + int(res[i+1]) == 3:
                res[i+1] = '1'
                res[i] = '1'
            elif int(a[i]) + int(b[i]) + int(res[i+1]) == 2:
                res[i+1] = '0'
                res[i] = '1'
            elif int(a[i]) + int(b[i]) + int(res[i+1]) == 1:
                res[i+1] = '1'
            else:
                res[i+1] = '0'

        for i in range(len(res)):
            if res[i] != '0':
                res = res[i:]
                break
            elif i == len(res) -1:
                return "0"
        tmp = ''.join(res)
        return tmp


if __name__ == '__main__':
    sol = Solution()
    output = sol.addBinary("100", "110010")
    print(output)