class Solution:
    def islandPerimeter(self, grid: list) -> int:
        if not grid or len(grid) == 0:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res += 4
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2
        return res


if __name__ == '__main__':
    sol = Solution()
    output = sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    print(output)