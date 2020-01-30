print ('TicTacToe')
print ('Player 1 - O, Player 2 - X. Enter position in format [row;column]. Player 1 starts first.')

field = [
    ['','',''],
    ['','',''],
    ['','','']
]

    # playing field visualisation
def winDef(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
            print('boo1')


    # column validaion
    # for i in range(len(board)):
    #    for j in range(len(board[0])):
    #        if board[0][j] == board[1][j] == board[2][j]:
    #           return True

    # left diagonal validation
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " " :
        return True
        print('boo2')
    # right diagonal validation
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
        print('boo3')
    return False

def playerInput(board, counter):
    if counter % 2 != 0:
        print('Player 1:')
        inp = input('enter coordintes (row column)')
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        board[i][j] = 'O'
        print_field(board)
    elif counter % 2 == 0:
        print('Player 2:')
        inp = input('enter coordintes (row column)')
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        board[i][j] = 'X'
        print_field(board)

def play_game(board):
    counter = 1
    while winDef(board) is False:
        playerInput(board)
        winDef(board)
        print_field(board, counter)
        counter = counter + 1
        if winDef(board) is True:
            print ('Player' + 'win')

def print_field(board):p
    for i in range(len(board)):
        if i != 0:
            print("-----------")

        for j in range(len(board[0])):
            if j != 0:
                print(" | ", end = "")

            if j == 2:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_field(field)
play_game(field)