# ____ WELCOME MESSAGE ____
print ('\n' + '\033[1;33mHello, let\'s play a game of tic-tac-toe \033[0;0m ⌗ ⌗ ⌗ ! 😁 ')
print("""\nHere are the game rules:
1. Two Players: Player X and Player O.
2. Player X starts the game.
3. Take turns to place marker on any vacant spot.
4. Get three of your markers in a row (horizontally, vertically or diagonally) to win the game.
    """)


# ____ ASK FOR NAMES OF PLAYER1 AND PLAYER2 ____
playerX = input("\t" + "Enter name for Player X :" +"\t")
playerX = playerX.capitalize() # Initial capitalize the name
playerO = input("\n" + "\t" + "Enter name for Player O :"+"\t")
playerO = playerO.capitalize() # Initial capitalize the name


# ____ START GAME ____
print("\n" + "\t" + playerX + "  vs  " + playerO + "." + " Let the game begin!")
print("\n" + "\t" + playerX + ", " + "you are X.  " + playerO + ", " + "you are O.")


# ____ CREATE THE BOARD ____
square = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# ____ DISPLAYS THE BOARD ____
def board():
  print("\n")
  print("\t" + "\t" + square[0] + " ⎢ " + square[1] + " ⎢ " + square[2])
  print("\t" + "\t" + "⏤⏤⏤⏤⏤⏤⏤⏤⏤")
  print("\t" + "\t"  + square[3] + " ⎢ " + square[4] + " ⎢ " + square[5])
  print("\t" + "\t" + "⏤⏤⏤⏤⏤⏤⏤⏤⏤")
  print("\t" + "\t" + square[6] + " ⎢ " + square[7] + " ⎢ " + square[8])
  print("\n")


# ____ PLAYER TURN ____
turn = 0
current_player = playerX
current_symbol = "X"

while turn < 9:
    board()
    input_square = input("\t" + current_player + ", select a square (1-9):" + "\n")
    input_square_int = int(input_square)
    square_index = input_square_int - 1
    if (square[square_index] == "X") or (square[square_index] == "O"):
        print(current_player + ", you selected a filled square. Try again. Select a square (1-9):")
    square[square_index] = current_symbol
    turn = turn + 1
    if current_player == playerX:
        current_player = playerO
        current_symbol = "O"
    else:
        current_player = playerX
        current_symbol = "X"
    if (square[0] != None) and (square[0] == square[1]) and (square[1] == square[2]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> First row horizontal\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[3] != None) and (square[3] == square[4]) and (square[4] == square[5]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> Middle row horizontal\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[6] != None) and (square[6] == square[7]) and (square[7] == square[8]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> Last row horizontal\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[0] != None) and (square[0] == square[3]) and (square[3] == square[6]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> First row vertical\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[1] != None) and (square[1] == square[4]) and (square[4] == square[7]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> Middle row vertical\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[2] != None) and (square[2] == square[5]) and (square[5] == square[8]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> Last row vertical\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[0] != None) and (square[0] == square[4]) and (square[4] == square[8]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> Left diagonal\033[0;0m')
        print("Game Over!" + "\n")
        exit()
    if (square[2] != None) and (square[2] == square[4]) and (square[4] == square[6]):
        board()
        print ('\n' + '\033[1;33mCongratulations! You have won! -> Right diagonal\033[0;0m')
        print("Game Over!" + "\n")
        exit()



# STEP 1: Create a list of squares [DONE]
# STEP 2: Create a board and name each of the squares. [DONE]
# STEP 3: Allocate X to Player1 [DONE]
# STEP 4: Allocate O to Player2 [DONE]
# STEP 5: If X turn == True:
    # hand game to X
    # place X on square when X inputs number
# STEP 6: If Player2 turn == place O on square
# The numbers players select
# STEP 7: Stop game when one of the players wins game
# STEP 8: Ask if players want to play again
# If yes, restart game
# If no, quit game
# Keep displaying new board when player's turn

