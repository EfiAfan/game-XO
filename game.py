board = [1,2,3,4,5,6,7,8,9]
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|",board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

draw_board(board)

play = 0

while play != 1:
    player1 = int(input())
    board[player1 - 1] = 'x'
    draw_board(board)
    player2 = int(input())
    board[player2 -1] = 'o'
    draw_board(board)