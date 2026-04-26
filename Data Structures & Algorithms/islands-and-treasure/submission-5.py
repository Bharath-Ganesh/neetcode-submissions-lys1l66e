class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        bfs = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs.append((row, col, 0))
        
        dirR = [-1, 0, 1, 0]
        dirC = [0,  1, 0, -1]
        while bfs:
            r, c, dis = bfs.popleft()
            for i in range(4):
                row = r + dirR[i]
                col = c + dirC[i]
                if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] in (0, -1):
                    continue
                if grid[row][col] > (dis + 1):
                    grid[row][col] = dis + 1 
                    bfs.append((row, col, dis + 1))
        
