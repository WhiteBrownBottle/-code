class Solution:
    def fizzBuzz(self, n: int) -> list:
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

if __name__ == '__main__':
    sol = Solution()
    output = sol.fizzBuzz(70)
    print(output)