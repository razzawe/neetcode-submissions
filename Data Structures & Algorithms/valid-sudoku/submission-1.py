class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Checking Quadrants:
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = set()
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        val = board[r][c]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        #Checking rows/cols:
    
        for i in range (9): # ROW
            row_counts = {i : 0 for i in range(1, 10)}
            col_counts = {i : 0 for i in range(1, 10)}
            for j in range(9): #COL
                #Row Check:
                if(board[i][j]) != '.':
                    if(row_counts[int(board[i][j])]) == 1:
                        return False
                    else:
                        row_counts[int(board[i][j])] += 1

                #Col Check:
                if(board[j][i]) != '.':
                    if(col_counts[int(board[j][i])]) == 1:
                        return False
                    else:
                        col_counts[int(board[j][i])] += 1
        return True
