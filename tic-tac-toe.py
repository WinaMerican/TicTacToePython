#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

# The Game Board
def newBoard():
     return {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }
board = newBoard()

#mark the board with user input
def markBoard(position, mark):
    board[position] = mark
    return True


#print the game board
def printBoard():
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[7] + " | " + board[8] + " | " + board[9])
    

# check for wrong input:
# user is entering invalid position or position is out of bound
# position is already occupied
def validateMove(position):
    position = int(position)
    if (position) in board and board[position] not in ["X","O"]:
        return True
    else:
        return False

#list of all the combinations of winning
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

#implement a logic to check if the previous winner just win
def checkWin(player):
    for combination in winCombinations:
        if all(board[position] == player for position in combination):
            return True
    return False

# implement a function to check if the game board is already full (tie)
def checkFull():
    for key in board:
        if board[key] not in ["X","O"]:
            return False
    return True

#start the game
def startGame():
    global board
    gameEnded = False
    currentTurnPlayer = 'X'

    # entry point of the whole program
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')

    # 1. Ask for user input and validate the input 
    # 2. Update the board
    # 3. Check win or tie situation
    # 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        try:
            move = int(move)
            if not validateMove(move):
                print("Invalid move")
                continue
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        markBoard(move, currentTurnPlayer)
        printBoard()

        if checkWin(currentTurnPlayer):
            print("Player " + currentTurnPlayer + " wins!")
            gameEnded = True
        elif checkFull():
            print("Tie!")
            gameEnded = True
        else:
            currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'

#option to replay the game
    replay = input("Do you want to play again? (y/n):").lower()
    if replay == "y":
        board = newBoard()
        startGame()
    else:
        print("Thank you for playing!")

startGame()