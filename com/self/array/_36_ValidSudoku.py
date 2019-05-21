class Solution:
    #Runtime: 52 ms, faster than 80.94% of Python3 online submissions for Valid Sudoku.
    #Memory Usage: 13.3 MB, less than 10.67% of Python3 online submissions for Valid Sudoku.
    def isValidSudoku(self, board) -> bool:
        n = len(board)
        for i in range(n):
            d_col = {}
            d_row = {}
            for j in range(n):
                if board[i][j] in d_row:
                    return False
                elif board[i][j] != ".":
                    d_row[board[i][j]] = True

                if board[j][i] in d_col:
                    return False
                elif board[j][i] != ".":
                    d_col[board[j][i]] = True
        for i in range(0, n):
            d = {}
            j_add = 3 * (i // 3)
            k_add = 3 * (i % 3)
            for j in range(3):
                for k in range(3):
                    if board[j_add + j][k_add + k] in d:
                        return False
                    elif board[j_add + j][k_add + k] != ".":
                        d[board[j_add + j][k_add + k]] = True
        return True


if __name__ == '__main__':
    t = Solution();
    input = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(t.isValidSudoku(input))
