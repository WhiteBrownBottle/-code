# 不会
class Solution:
    def countAndSay(self, n: int) -> str:
        arr = ["1"]
        for i in range(n-1):
            ans =""
            j = 0
            while j < len(arr[i]):
                num = arr[i][j]
                time = 0
                while j < len(arr[i]) and num == arr[i][j]:
                    j += 1
                    time += 1
                ans += str(time) + num
            arr.append(ans)
        return arr[n-1]

if __name__ == '__main__':
    sol = Solution()
    output = sol.countAndSay(5)
    print(output)