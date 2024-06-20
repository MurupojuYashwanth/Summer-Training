def check(row,col,no):
    for i in range(9):
        if board[i][col]==no:
            return False
        if board[row][i]==no:
            return False
    return True
def sudoko(row,col):
    if row==n:
         return
    if col==n:
        sudoko(board,row+1,0)
    if board[i][j]=='.':
        for i in range(1,10):
            if check(row,col,i):
                board[row][col]=i
                
         
 board = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]
 n=len(board)
 sudoko(0,0)