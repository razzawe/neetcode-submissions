class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] # create mxn grid (extra row and extra col for extra 0's)
        dp[m-1][n-1] = 1 # initialize bottom right to 1

        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                dp[i][j] += dp[i+1][j] + dp[i][j+1] # add bottom cell and right cell for each i,j index

        return dp[0][0]