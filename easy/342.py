import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        i = math.log10(num) / math.log10(4)
        return i == int(i)