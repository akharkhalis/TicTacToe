test_field = [
    ['x', 'o', 'x'],
    ['', 'o', 'o'],
    ['x', '', 'o']
]


def row_validation(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
                return True

def column_validation(board):
    # column validaion
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[0][j] == board[1][j] == board[2][j]:
                return True

def ldiagonal_validation(board):
    # left diagonal validation
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
        print('boo2')

def rdiagonal_validation(board):
    # right diagonal validation
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
        print('boo3')

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

win_def(test_field)
print(win_def(test_field))


