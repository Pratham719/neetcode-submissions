class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            col_seen=set()
            row_seen=set()
            for j in range(len(board[i])):
                row_value=board[i][j]
                col_value=board[j][i]

                if row_value != ".":
                    if row_value in row_seen:
                        return False
                    row_seen.add(row_value)
                
                if col_value != ".":
                    if col_value in col_seen:
                        return False
                    col_seen.add(col_value)

            for squere in range(9):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        row=(squere//3)*3+i
                        col=(squere%3)*3+j

                        if board[row][col]==".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])

        return True
sol=Solution()
board =[["1","2",".",".","3",".",".",".","."],
        ["4",".","1","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))