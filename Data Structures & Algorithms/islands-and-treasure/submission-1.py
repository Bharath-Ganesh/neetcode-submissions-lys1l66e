class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        treasure_chest_queue = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasure_chest_queue.append((0, row, col))

        # U, R, D, L
        visited = [[False] * cols for i in range(rows)]
        dirR = [-1, 0, 1, 0]
        dirC = [ 0, 1, 0, -1]
        while treasure_chest_queue:
            dist, r, c = treasure_chest_queue.popleft()
            visited[r][c] = True
            for i in range(4):
                nRow = r + dirR[i]
                nCol = c + dirC[i]
                if not (nRow < 0 or nCol < 0 or nRow >= rows or nCol >= cols or grid[nRow][nCol] in (-1,0)):
                    if grid[nRow][nCol] > dist + 1:
                        grid[nRow][nCol] = dist + 1
                        treasure_chest_queue.append((grid[nRow][nCol], nRow, nCol))
        
        
                
        