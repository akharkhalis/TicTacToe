
board = [
    ['o','x','x'],
    ['','o','o'],
    ['x','','o']
]
# column validaion
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[0][j] == board[1][j] == board[2][j] != ' ' :
            print ('Win2')

# row validation
for i in range(len(board)):
   if board[i][0] == board[i][1] == board[i][2]:
       print("win1")

#left diagonal validation
if board[0][0] == board[1][1] == board[2][2]:
    print ('Win3')

#right diagonal validation
if board[0][2] == board[1][1] == board[2][0]:
    print ('Win4')
print(board)

