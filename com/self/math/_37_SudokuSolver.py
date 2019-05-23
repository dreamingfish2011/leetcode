class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        likely = [[[], [], [], [], [], [], [], [], []] for i in range(9)]
        for i in range(9):
            for j in range(9):
                likely[i][j] = {'1': True, '2': True, '3': True, '4': True, '5': True, '6': True, '7': True, '8': True,
                                '9': True}
        count = 81
        while count >0:
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        likely[i][j] = {board[i][j]: True}
                        count -= 1
                    self.generateLikelyDict(likely, board, i, j)
            # self.DFS(likely, board, 0, 0)

    def generateLikelyDict(self, likely, board, i, j):
        for k in range(9):
            if board[i][j] in likely[i][k]:
                del likely[i][k][board[i][j]]
                # if len(likely[i][k]) == 1:
                #     board[i][k] = likely[i][k].items()[0]
            if board[i][j] in likely[k][j]:
                del likely[k][j][board[i][j]]
                # if len(likely[k][j]) == 1:
                #     board[k][j] = likely[k][j].items()[0]
            if board[i][j] in likely[int(i / 3) * 3 + int(k / 3)][int(j / 3) * 3 + k % 3]:
                del likely[int(i / 3) * 3 + int(k / 3)][int(j / 3) * 3 + k % 3][board[i][j]]
                # if len(likely[int(i / 3) * 3 + int(k / 3)][int(j / 3) * 3 + k % 3]) == 1:
                #     board[int(i / 3) * 3 + int(k / 3)][int(j / 3) * 3 + k % 3] = \
                #     likely[int(i / 3) * 3 + int(k / 3)][int(j / 3) * 3 + k % 3].items()[0]


    def DFS(self, likely, board, row, col):
        if row == 9:
            return True
        if col == 9:
            return self.DFS(likely, board, row + 1, 0)
        if board[row][col] != ".":
            return self.DFS(likely, board, row, col + 1)
        # charArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for c in likely[row][col]:
            # if self.isValidNumber(row, col, board, c):
            board[row][col] = c
            # self.generateLikelyDict(likely, board, row, col)
            if self.DFS(likely, board, row, col + 1):
                return True
            # del likely[row][col][c]
            board[row][col] = "."
        return False


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
    t.solveSudoku(input)
    for i in range(9):
        print("-".join(input[i]))
