class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp数据记录网格大小为i*j时唯一路径数
        dp = [[1] * n for i in range(m)]
        dp[0][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m - 1][n - 1]

    def uniquePathsByMath(self, m: int, n: int) -> int:
        # 数学方法解决
        # R m-1次  D  n-1次
        if n > m:
            m, n = n, m
        multi = 1
        divno =1
        for i in range(n - 1):
            multi *= (m + n - 2 - i)
            divno *= n - 1 - i
        return int(multi/divno)


if __name__ == "__main__":
    test = Solution()
    print(test.uniquePaths(7, 3))
    print(test.uniquePathsByMath(6, 4))
