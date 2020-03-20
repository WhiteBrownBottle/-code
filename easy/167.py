class Solution:
    def twoSum(self, numbers: list, target: iwnt) -> list:
        for i in range(0, len(numbers)):
            dif = target - numbers[i]
            if dif in numbers.pop(i):
                label1 = i+1
                label2 = numbers.index(dif) + 1
                return [label1, label2]