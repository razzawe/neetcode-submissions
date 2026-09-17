class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def add(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == -1):
                return
            q.append([r, c])
            visited.add((r,c))

        #treasures in initial queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        dist = 0 

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add(r+1,c)
                add(r,c+1)
                add(r-1,c)
                add(r,c-1)
            dist += 1
    



