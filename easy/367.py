class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return num ** 0.5 == int(num**0.5)