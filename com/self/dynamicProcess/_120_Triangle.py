class Solution:
    def minimumTotal(self, triangle) -> int:
        M = len(triangle)
        if M == 0:
            return 0
        for layer in range(M - 2, -1, -1):
            for i in range(0, layer+1):
                triangle[layer][i] += min(triangle[layer + 1][i], triangle[layer + 1][i + 1])
        return triangle[0][0]


if __name__ == "__main__":
    test = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(test.minimumTotal(triangle))
