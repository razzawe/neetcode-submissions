class Solution:

   
  
  
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # num(rows) = m, num(cols) = n
        def dfs(r,c,atlPac,visited):
            if r == 0 or c == 0:
                atlPac.add(0)

            if r == ROWS - 1 or c == COLS - 1:
                atlPac.add(1)
            
            if (r, c) in visited:
                return
            
            visited.add((r,c))

            # Move up
            if r > 0 and heights[r-1][c] <= heights[r][c]:
                dfs(r-1, c, atlPac, visited)
            
            # Move down
            if r < ROWS - 1 and heights[r + 1][c] <= heights[r][c]:
                dfs(r + 1, c, atlPac, visited)

            # Move left
            if c > 0 and heights[r][c - 1] <= heights[r][c]:
                dfs(r, c - 1, atlPac, visited)

            # Move right
            if c < COLS - 1 and heights[r][c + 1] <= heights[r][c]:
                dfs(r, c + 1, atlPac, visited)

        ROWS, COLS = len(heights), len(heights[0])
        flowCells = []
        for i in range(ROWS):
            for j in range(COLS):
                atlPac = set()
                visited = set()
                dfs(i,j,atlPac,visited)

                if len(atlPac) == 2:
                    flowCells.append([i, j])

        return flowCells




                

        