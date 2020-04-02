class Solution:
    def getSum(self, a: int, b: int) -> int:
        nums = []
        nums.append(a)
        nums.append(b)
        return sum(nums)


class Solution2:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
