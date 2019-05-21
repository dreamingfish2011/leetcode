
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in matrix:
            l.reverse()


if __name__ == '__main__':
    t = Solution();
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    t.rotate(input_matrix)
    print(input_matrix)
