class Solution(object):
    def solve(self, board):
        if not board:
            return

        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    stack.append((i,j))

        while stack:
            x, y = stack.pop()
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = 'V'
                stack.append((x-1, y))
                stack.append((x+1, y))
                stack.append((x, y-1))
                stack.append((x, y+1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'

