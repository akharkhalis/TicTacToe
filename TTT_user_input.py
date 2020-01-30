field = [
    ['','',''],
    ['','',''],
    ['','','']
]
counter = 1

def print_field(board):
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

def user_input(user,board):
    print(user)
    inp = input('enter coordintes (row column)')
    i = int(inp[0]) - 1
    j = int(inp[1]) - 1

    if board[i][j] != '':
        inp = input('This position is already used, choose another one:')
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        print_field(board)
    else:
        if user == "Player 1:":
            board[i][j] = 'o'
        else:
            board[i][j] = 'x'
        print_field(board)

while counter < 10:
    if counter % 2 != 0:
        user = "Player 1:"
        user_input(user, field)

    elif counter % 2 == 0:
        user = "Player 2:"
        user_input(user, field)
    elif counter == 10:
        print('Draw')
    counter = counter + 1