class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    stack = [(i,j)]
                    is_subisland = True
                    
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                            grid2[x][y] = 0
                            if grid1[x][y] == 0:
                                is_subisland = False
                            stack.append((x-1, y))
                            stack.append((x+1, y))
                            stack.append((x, y-1))
                            stack.append((x, y+1))
                    
                    if is_subisland:
                        count += 1
        
        return count
