class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        #m行  n列
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if n==0  :
            return 0
        for i in range(0,n):
            if obstacleGrid[0][i] <=0 :
                obstacleGrid[0][i] = -1
            else :
                break
        for i in range(0,m):
            if obstacleGrid[i][0] <= 0 :
                obstacleGrid[i][0] = -1
            else :
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] <=0 :
                    obstacleGrid[i][j] = min(obstacleGrid[i - 1][j] ,0) + min(obstacleGrid[i][j - 1] ,0)
        return max(0,-obstacleGrid[m - 1][n - 1])


if __name__ == "__main__":
    test = Solution()
    print(test.uniquePathsWithObstacles([[1,1]]))
