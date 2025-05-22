from random import choice

board = [[1,2,3],[4,5,6],[7,8,9]]
freeFields = []



def display_board(board):
    print("+---+---+---+")
    for row in board:
        print("| {} | {} | {} |".format(*row))
        print("+---+---+---+")
    
def enter_move(board):
    BotMove = choice(freeFields)
    if BotMove>6:
        i=board[2].index(BotMove)
        board[2][i]="X"
    elif BotMove<4:
        i=board[0].index(BotMove)
        board[0][i]="X"
    else:
        i=board[1].index(BotMove)
        board[1][i]="X"
    make_list_of_free_fields(board)    


def make_list_of_free_fields(board):
    freeFields.clear()
    for i in range(3):
        for j in board[i]:
            if type(j) is int:
                freeFields.append(j)

def victory_for(board, sign):
    res = None
    if sign == "X":
        res = 3
    if sign == "0":
        res = 4
    crossList1=[]
    crossList2=[]
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return res
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return res
        if board[i][i] == sign:
            crossList1.append(i)
        if board[2-i][2-i] == sign:
            crossList2.append(i)
    if len(crossList1)==3 or len(crossList2)==3:
        return res
    return None
        


def draw_move(board):
    userMove = int(input("Enter your move: "))
    if userMove in freeFields:
        if userMove>6:
            i=board[2].index(userMove)
            board[2][i]="0"
        elif userMove<4:
            i=board[0].index(userMove)
            board[0][i]="0"
        else:
            i=board[1].index(userMove)
            board[1][i]="0"
        make_list_of_free_fields(board) 
    else:
        print("Your choice out of the range.\nYou can't chooce position where X!!!")
        draw_move(board)

make_list_of_free_fields(board)
while len(freeFields):
    display_board(board)
    enter_move(board)
    display_board(board)
    if len(freeFields)>1:
        draw_move(board)
    if victory_for(board,"0")==4:
        print("You win")
        break
    if victory_for(board,"X")==3:
        print("Computer win")
        break


print()