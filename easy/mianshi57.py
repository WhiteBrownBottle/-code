class Solution:
    def findContinuousSequence(self, target: int):
        all = []
        for i in range(1, target):
            sum = i
            instance = []
            instance.append(i)
            for j in range(i+1, target):
                sum += j
                instance.append(j)
                if sum == target:
                    all.append(instance)
                    break
                elif sum > target:
                    break
        return all

if __name__ == '__main__':
    sol = Solution()
    print(sol.findContinuousSequence(9))
