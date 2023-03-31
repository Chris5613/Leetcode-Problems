class Solution(object):
    def numIslands(self, grid):

        if not grid:
            return 0 
        
        m , n = len(grid), len(grid[0])
        count = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i,j)]
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            grid[x][y] = 0

                            stack.append((x-1,y))
                            stack.append((x+1,y))
                            stack.append((x,y-1))
                            stack.append((x,y+1))
        return count