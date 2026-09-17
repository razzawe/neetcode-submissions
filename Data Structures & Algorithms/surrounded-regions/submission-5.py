class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        #First idea:
            #need dfs to check if edge of region is X
            #run for loop through cell which is an O, if already checked, we ignore (visited set)

        #Second idea (As implemented below)
            #look for the ones that DONT work, then look through entire array and set all remaining o's that are NOT in visited to X
        

        visited = set()
      
        def dfs(r,c): #checking which nodes are connected to edges (impossible to be surrounded)
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] == 'X':
                return

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            

        for c in range(COLS):  # this is O(mn) because there is a visited set, making it impossible for n*(o(mn))
            if board[0][c] == "O": #check all top edges for O's
                dfs(0, c)
            if board[ROWS-1][c] == "O": # check all bottom edges for O's
                dfs(ROWS-1, c)
        
        for r in range(ROWS): # O(mn), same reason as above&
            if board[r][0] == "O": #check all left edges for O's
                dfs(r, 0) # O(m*n)
            if board[r][COLS-1] == "O": #check all right edges for O's
                dfs(r, COLS-1)
        
        for r in range(ROWS): #O(mn)
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

        #So, 3*(O(mn)) = O(mn)