class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        minutes = 0
        healthy = 0

        def rotCell(r,c):
            nonlocal healthy
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] != 1):
                return
            q.append([r,c])
            visited.add((r,c))
            healthy -= 1

        #rotten fruits to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                if grid[r][c] == 1:
                    healthy += 1


        while q and healthy:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                rotCell(r+1,c)
                rotCell(r,c+1)
                rotCell(r-1,c)
                rotCell(r,c-1)
            minutes += 1
        return minutes if healthy == 0 else -1

