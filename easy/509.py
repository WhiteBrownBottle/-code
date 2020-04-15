class Solution:
    def fib(self, N: int) -> int:
        A = [0, 1]
        for i in range(2, N + 1):
            A.append(A[i-1] + A[i-2])
        return A[N]