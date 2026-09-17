class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # function to see if we can add cell to queue and add if we can
        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r,c])

        
        # add all treasure spots to initial queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))

        dist = 0 #starting with the treasure spots 

        while q: 
            for i in range(len(q)): #only runs for the length of queue at start of this for loop (so allows us to compute i.e. dist = 0 then dist = 1 and so on...)

                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            dist += 1
        
