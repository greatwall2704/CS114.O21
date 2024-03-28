def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            return True
    
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    
    if board[2][0] == board[1][1] == board[0][2]:
        return True
    return False

board = [list(map(int, input().split())) for _ in range(3)]

n = int(input())

list_numbers = []
for _ in range(n):
    list_numbers.append(int(input()))

for number in list_numbers:
    for i in range(3):
        for j in range(3):
            if board[i][j] == number:
                board[i][j] = 0

if check_win(board):
    print("Yes")
else:
    print("No")
