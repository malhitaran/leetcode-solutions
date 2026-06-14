# Valid Sudoku (Medium)
# https://leetcode.com/problems/valid-sudoku/
# Accepted 2026-06-14 — Python3, runtime 3 ms, memory 19.2 MB
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''

        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

        given this input, we can validate it across 3 constraints

        firstly values have to be unique on the top row

        maybe create a set each time check if its already in set return false

        do the same for columns

        then we work out the final step

        '''
        #check 1
        rows=9
        cols=9
        ourSet=set()
        for i in range(rows):
            ourSet.clear()
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if board[i][j] in ourSet:
                    return False
                else:
                    ourSet.add(board[i][j]) 

        #check 2
        for i in range(cols):
            ourSet.clear()
            for j in range(rows):
                if board[j][i] == ".":
                    continue
                if board[j][i] in ourSet:
                    return False
                else:
                    ourSet.add(board[j][i])
        
        #check 3(the 3x3)
        '''
        we can put each 9 block into sets
        this tells us the box its in
        '''
        setList = [set() for _ in range(9)]
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==".":
                    continue
                elif board[i][j] in setList[((i//3) *3 +(j//3))]:
                    return False
                else:
                    setList[((i//3) *3 +(j//3))].add(board[i][j])

    
        return True
