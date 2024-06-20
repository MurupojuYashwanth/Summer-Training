def printBoard(board):
    print("-")
    for i in board:
        print(i)
def placeOrNot(board,row,col):
    if row==ro:
        return False
    if col==co:
        return False
    i=row-1
    #up
    while i>=0:
        if board[i][col]=='Q':
            return False
        i-=1
    #left diagonal
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1
    #right diagonal
    i=row-1
    j=col+1
    while i>=0 and j<len(board):
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1
    return True
def nQueen(board,row):
    global c
    if row==len(board):
        c+=1
        return board
    if row!=ro:
        for j in range(len(board)):
            if placeOrNot(board,row,j):
                board[row][j]='Q'
                return nQueen(board,row+1)
            board[row][j]='-'
        return nQueen(board,row+1)
    else:
        return nQueen(board,row+1)
    
n=5
ro=1
co=3
c=0
board =[['-']*n for _ in range(n)]
res = nQueen(board,0)
for i in res:
    print(i)
print(c)

