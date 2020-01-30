field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# printing nice shaped playing field
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

# validation for win definition row, column, and diagonals starting from left top corner and right top corner
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

# win definition summary :)
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

# transforming user input from f.e. 12 to the board[0][1]
def user_input(user,board):
    print(user)
    inp = input('enter coordintes (row column)')
    i = int(inp[0]) - 1
    j = int(inp[1]) - 1

    # validation of input to the filled cells
    # needs to add loop for 'This position is already used, choose another one:',
    # at the moment it works only once and than swithces to the second played
    if board[i][j] != '':
        inp = input('This position is already used, choose another one:')
        # duplicated code, replace with function
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


# play game, here is a total mess, need to think how to redo this part
# add 'Player # win'
def play_game(board):
    counter = 1
    while win_def(board) is not True:
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
print('Win!')
