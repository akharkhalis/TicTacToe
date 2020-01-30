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

while counter < 10:
    if counter % 2 != 0:
        print('Player 1:')
        inp = input('enter coordintes (row column)')
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        field[i][j] = 'O'
        print_field(field)
    elif counter % 2 == 0:
        print('Player 2:')
        inp = input('enter coordintes (row column)')
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        field[i][j] = 'X'
        print_field(field)
    elif counter == 10:
        print('Draw')
    counter = counter + 1