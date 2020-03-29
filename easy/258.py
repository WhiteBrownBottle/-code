class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        while num > 10:
            next = 0
            while num != 0:
                next += num % 10
                num //= 10
            num = next
        return num

