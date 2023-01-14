board = [1,2,3,4,5,6,7,8,9]

#Рисование доски
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")
        
draw_board(board)
play = 0 #Если переменная становится ==1, то игра прекращается, например при победе
history = [] #История ходов, проверяет на то, не занято ли поле

while play != 1:
    count = 0 #счётчик ходов для условия "Ничья"
    count1 = 0 #аналогично, но для второго игрока
    player1 = int(input()) #ход игрока 1
    for i in range(len(history)): #цикл на проверку занятого поля
        if player1 == history[i]:
            print('Поле занято!')
            while player1 == history[i]:
                player1 = int(input())
    board[player1 - 1] = 'x'
    draw_board(board)
    history.append(player1)
    #условия победы
    if board[0] == board[1] and board[0] == board[2]:
        play = 1
    if board[3] == board[4] and board[3] == board[5]:
        play = 1
    if board[6] == board[7] and board[6] == board[8]:
        play = 1
    if board[0] == board[3] and board[0] == board[6]:
        play = 1
    if board[1] == board[4] and board[1] == board[7]:
        play = 1
    if board[2] == board[5] and board[2] == board[8]:
        play = 1
    if board[0] == board[4] and board[0] == board[8]:
        play = 1
    if board[2] == board[4] and board[2] == board[6]:
        play = 1
    for i in range(len(board)): #условия ничьей
        if board[i] == i+1:
            count += 1
            if count == 0:
                break
    if play == 1:
        print("Победа крестиков!")
        break
    if count == 0:
        print("Ничья!")
        break
    player2 = int(input())
    for i in range(len(history)):
        if player2 == history[i]:
            print('Поле занято!')
            while player2 == history[i]:
                player2 = int(input())
    board[player2 -1] = 'o'
    draw_board(board)
    history.append(player2)
    if board[0] == board[1] and board[0] == board[2]:
        play = 1
    if board[3] == board[4] and board[3] == board[5]:
        play = 1
    if board[6] == board[7] and board[6] == board[8]:
        play = 1
    if board[0] == board[3] and board[0] == board[6]:
        play = 1
    if board[1] == board[4] and board[1] == board[7]:
        play = 1
    if board[2] == board[5] and board[2] == board[8]:
        play = 1
    if board[0] == board[4] and board[0] == board[8]:
        play = 1
    if board[2] == board[4] and board[2] == board[6]:
        play = 1
    for i in range(len(board)):
        if board[i] == i+1:
            count1 += 1
            if count1 == 0:
                break
    if play == 1:
        print("Победа ноликов!")
        break
    if count1 == 0:
        print("Ничья!")
        break