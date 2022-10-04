'''
Author-Ashutosh(0Pixel0).
'''
board = [[0 for i in range(3)] for j in range(3)]
turn = 0  # zero first.

def print_board():
    for x in range(3):
        for y in range(3):
            exp = '.'
            if (board[x][y] == 1):
                exp = "O"
            elif (board[x][y] == 2):
                exp = "X"
            print(f" {exp} ", end="")
        print("\n------------");

def full():
    for  x in range(3):
        for y in range(3):
            if(board[x][y]==0):
                return False;
    return True;

def cols():
    for j in range(3):
        if(board[0][j]==board[1][j] and board[1][j]==board[2][j] and board[0][j]!=0):
            return board[0][j];
    return 0;

def rows():
    for j in range(3):
        if(board[j][0]==board[j][1] and board[j][1]==board[j][2] and board[j][0]!=0):
            return board[j][0];
    return 0;

def diag():
    if(board[0][0]==board[1][1]==board[2][2] and board[0][0]!=0):
        return board[0][0];
    if(board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0):
        return board[0][0];
    return 0;

def check():
    if(cols()==0 and rows()==0 and diag()==0):
        return 0;
    if(cols()!=0):
        return cols();
    if(rows()!=0):
        return rows();
    if(diag()!=0):
        return diag();

while (full()==False):
    if (turn == 0):
        pos = int(input('enter position for O:'))
        pos -= 1
        if(board[pos//3][pos%3] != 0 or pos > 8 or pos <0):
            print("Enter a valid position.")
            continue;
        board[pos//3][pos % 3] = 1
        turn = 1
    else:
        pos = int(input('enter position for X:'))
        pos -= 1
        if(board[pos//3][pos%3] != 0 or pos > 8 or pos <0):
            print("Enter a valid position.")
            continue;
        board[pos//3][pos % 3] = 2
        turn = 0
    print_board()
    winner=check();
    if(winner==1):
        print("PLAYER O WON!!!");
        break;
    elif(winner==2):
        print("PLAYER X WON!!!");
        break;
    elif(full()):
        print("GAME IS DRAWN :(");
        break;



    
