from TTT_user_input import user_input
field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]


def print_field(board):
    for i in range(len(board)):
        if i != 0:
            print("-----------")

        for j in range(len(board[0])):
            if j != 0:
                print(" | ", end="")

            if j == 2:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def row_validation(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return True
        else:
            return False


def column_validation(board):
    # column validaion
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "":
                return True
            else:
                return False


def ldiagonal_validation(board):
    # left diagonal validation
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    else:
        return False


def rdiagonal_validation(board):
    # right diagonal validation
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return True
    else:
        return False


def win_def(board):
    if row_validation(board) is True:
        return True
    elif column_validation(board) is True:
        return True
    elif ldiagonal_validation(board) is True:
        return True
    elif rdiagonal_validation(board) is True:
        return True
    else:
        return False

def user_input(user,board):
    print(user)
    inp = input('enter coordintes (row column)')
    i = int(inp[0]) - 1
    j = int(inp[1]) - 1

    if board[i][j] != '':
        inp = input('This position is already used, choose another one:')
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        if user == "Player 1:":
            board[i][j] = 'o'
        else:
            board[i][j] = 'x'
        print_field(board)
    else:
        if user == "Player 1:":
            board[i][j] = 'o'
        else:
            board[i][j] = 'x'
        print_field(board)

def play_game(board):
    counter = 1
    while not win_def(board):
        print_field(board)
        if counter % 2 != 0:
            user = "Player 1:"
            user_input(user, field)
        elif counter % 2 == 0:
            user = "Player 2:"
            user_input(user, field)
        elif counter == 10:
            print('Draw')
        counter = counter + 1


#print_field(field)
play_game(field)
print(win_def(field))
