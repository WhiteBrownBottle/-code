class Solution:
    def plusOne(self, digits: list) -> list:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10**(len(digits)-1-i)
        num += 1
        new_digits = list(str(num))
        for j in range(len(new_digits)):
            new_digits[j] = int(new_digits[j])
        return new_digits




if __name__ == '__main__':
    sol = Solution()
    output = sol.plusOne([1,2,3])
    print(output)