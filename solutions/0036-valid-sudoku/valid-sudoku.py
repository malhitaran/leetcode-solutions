# Valid Sudoku (Medium)
# https://leetcode.com/problems/valid-sudoku/
# Accepted 2026-08-01 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        '''
        -we can do 3 sets
        -we can do one loop
        -theres a trick to see which box something is in

        our box set can be a tuple, of box num and num

        '''

        rowSet=set()
        colSet=set()
        boxSet=set()

        rows=len(board)
        cols=len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==".":
                    continue
                #calculate box
                box_index = (r // 3) * 3 + (c // 3)
                if (r, board[r][c]) in rowSet:
                    return False
                else:
                    rowSet.add((r, board[r][c]))
                if (c, board[r][c]) in colSet:
                    return False
                else:
                    colSet.add((c, board[r][c]))
                if (box_index, board[r][c]) in boxSet:
                    return False
                else:
                    boxSet.add((box_index, board[r][c]))
        return True

                #now we need to add to there sets
