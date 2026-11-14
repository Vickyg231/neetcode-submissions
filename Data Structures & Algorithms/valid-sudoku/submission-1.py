class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowC = {}
        colC = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in rowC:
                    rowC[board[i][j]] = i
                else:
                    return False
            rowC.clear()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] not in colC:
                    colC[board[j][i]] = j
                else:
                    return False
            colC.clear()
        square = {}
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] not in square:
                            square[board[row][col]] = col
                        else:
                            return False
                square.clear()
            return True

