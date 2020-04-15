class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        symbol = ''
        if num < 0:
            symbol = '-'
        reminder = []
        num = abs(num)
        while num > 0:
            reminder.insert(0, str(num % 7))
            num //= 7
        return symbol + ''.join(reminder)