
#initialize board list
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def DisplayBoard(board):
    for row in range(3):
        print(end= '\n')
        print("+-------+-------+-------+", end = "\n\n")
        for col in range(3):
            print("|   ",end = "")
            print(board[row][col], end = '   ')
        print("|")
    print("\n+-------+-------+-------+", end = "\n\n")


def EnterMove(board, sign):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    validinput = True

    while validinput:

        try:
            current_move = int(input("Please enter your move: "))
        except ValueError:
            continue

        for row in range(3):
            for col in range(3):
                if board[row][col] == current_move:
                    board[row][col] = sign
                    validinput = False
                    break


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #

    gameOver = True

    # check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        print("Player using ", sign, " is the winner")

    elif board[0][2] == board[1][1] == board[2][0]:
         print("Player using ", sign, " is the winner")

    # Check horizontal
    elif board[0][0] == board[0][1] == board[0][2]:
        print("Player using ", sign, " is the winner")

    elif board[1][0] == board[1][1] == board[1][2]:
         print("Player using ", sign, " is the winner")

    elif board[2][0] == board[2][1] == board[2][2]:
         print("Player using ", sign, " is the winner")

    # Check vertical
    elif board[0][0] == board[1][0] == board[2][0]:
         print("Player using ", sign, " is the winner")

    elif board[0][1] == board[1][1] == board[2][1]:
         print("Player using ", sign, " is the winner")

    elif board[0][2] == board[1][2] == board[2][2]:
         print("Player using ", sign, " is the winner")
    else:
        gameOver = False

    return gameOver


def MakeListOfFreeFields(board, player1, player2):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    Draw = False
    freeField=[]
    for row in range(3):
        for col in range(3):
            if ((board[row][col] == player1) or (board[row][col] == player2)) == False:
                freeField.append(board[row][col])

    if len(freeField) == 0:
        Draw = True
        return Draw


print("Lets play Tick Tack Toe")

Player1 = input("Player 1, Please choose your sign X or O: ")
Player2 = input("Player 2, Please choose another sign: ")

DisplayBoard(board)
Victory = False
Draw = False
counter = 0
while not Victory and not Draw:

    if counter % 2 == 0:
        sign = Player1
        currentPlayer = "Player 1"

    else:
        sign = Player2
        currentPlayer = "Player 2"

    print(currentPlayer, "'s turn ")
    print("Please select a free number between 1 to 9")

    EnterMove(board, sign)
    counter+=1
    DisplayBoard(board)
    Victory= VictoryFor(board, sign)
    Draw = MakeListOfFreeFields(board, Player1, Player2)
    if Victory == True:
        print("***********************")
        print(currentPlayer, " Wins")
        print("***********************")
    elif Draw == True:
        print("***********************")
        print("It's a draw")
        print("***********************")
        
