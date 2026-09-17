class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        res = []
        def dfs(r,c,visited,prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) #checking left side connected to pacific
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # checking right side connected to pacific
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) #checking top side connected to pacific
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) #checking bottom side connected to atlantic
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        
        return res
           
