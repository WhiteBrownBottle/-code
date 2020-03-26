class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        count = 1
        def isPrime(n:int):
            sqrt = int(n**0.5)+1
            for i in range(3, sqrt, 2):
                if n % i == 0:
                    return 0
            return 1

        for i in range(3, n, 2):
            count += isPrime(i)
        return count


class Solution2:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        prime_list = [False]*n
        count = 0
        for i in range(2, n):
            if not prime_list[i]:
                count += 1
                for j in range(i*2, n, i):
                    prime_list[j] = True
        return count





if __name__ == '__main__':
    sol = Solution2()
    output = sol.countPrimes(20)
    print(output)
