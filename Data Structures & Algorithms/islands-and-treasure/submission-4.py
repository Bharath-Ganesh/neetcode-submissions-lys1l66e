class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                # treasure hunt
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
        
        dirR = [-1, 0, 1, 0]
        dirC = [0, -1, 0, 1]
        visited = [[False] * cols for _ in range(rows)]
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col, distance = queue.popleft()
                visited[row][col] = True
                if grid[row][col] > distance:
                    grid[row][col] = distance
                
                for i in range(4):
                    nR = dirR[i] + row
                    nC = dirC[i] + col

                    if nR < 0 or nC < 0 or nR >= rows or nC >= cols or grid[nR][nC] == -1 or visited[nR][nC]:
                        continue
                    
                    queue.append((nR, nC, distance + 1))
        








