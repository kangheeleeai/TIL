# https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        grid = [[0 for _ in range(m)] for _ in range(n)] 
        queue = deque()
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        for row in range(n):
            for column in range(m):
                if mat[row][column] == 0: 
                    queue.append((row, column, 0))
                    visited[row][column] = True
           
        while queue:
            row, column, distance = queue.popleft()
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r, c = row + x, column + y
                if r in range(n) and c in range(m) and not visited[r][c]:
                    grid[r][c] = distance+1
                    queue.append((r, c, distance+1))
                    visited[r][c] = True
                    
        return grid
