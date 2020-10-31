# ____ WELCOME MESSAGE ____
print ('\n' + '\033[1;33mHello, let\'s play a game of tic-tac-toe \033[0;0m ⌗ ⌗ ⌗ ! 😁 ')
# print("\n" + "Hello, let's play a game of tic-tac-toe ⌗ ⌗ ⌗ ! 😁 ")
print("""\nHere are the game rules:
1. Two Players: Player X and Player O.
2. Player X starts the game.
3. Take turns to place marker on any vacant spot.
4. Get three of your markers in a row (horizontally, vertically or diagonally) to win the game.
    """)

# ____ CREATE THE BOARD ____
square = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# Note: Might want to add "0" and make it invisible to viewers due to indexing
# OR : playerInput = playerInput -1



def board():
  print("\n")
  print("\t" + "\t" + square[0] + " ⎢ " + square[1] + " ⎢ " + square[2])
  print("\t" + "\t" + "⏤⏤⏤⏤⏤⏤⏤⏤⏤")
  print("\t" + "\t"  + square[3] + " ⎢ " + square[4] + " ⎢ " + square[5])
  print("\t" + "\t" + "⏤⏤⏤⏤⏤⏤⏤⏤⏤")
  print("\t" + "\t" + square[6] + " ⎢ " + square[7] + " ⎢ " + square[8])
  print("\n")


# ____ ASK FOR NAMES OF PLAYER1 AND PLAYER2 ____
X = input("\t" + "Enter name for Player X :" +"\t")
X = X.capitalize() # Initial capitalize the name
O = input("\n" + "\t" + "Enter name for Player O :"+"\t")
O = O.capitalize() # Initial capitalize the name

players = [X, O] # Save the list of the players into a variable


# ____ START GAME ____
print("\n" + "\t" + X + "  vs  " + O + "." + " Let the game begin!")
print("\n" + "\t" + X + ", " + "you are X.  " + O + ", " + "you are O.")

# ____ DISPLAYS THE BOARD ____
board()


# ____ PLAYER TURN ____
def addX():
        playerInput = int(input("\t" + X + ", select a square (1-9):" + "\n"))
        playerInput = playerInput - 1
        square[playerInput] # Allocate playerInput to index number on list
        if (square[playerInput] == "X") or (square[playerInput] == "O"):
            playerInput = int(input("\t" + X + ", you selected a filled square. Try again. Select a square (1-9):" + "\n"))
        else:
            playerInput
            square[playerInput] # Allocate playerInput to index number on list
        square[playerInput] = "X"
        board()

def addO():
        playerInput = int(input("\t" + O + ", select a square (1-9):" + "\n"))
        playerInput = playerInput - 1
        square[playerInput] # Allocate playerInput to index number on list
        if (square[playerInput] == "X") or (square[playerInput] == "O"):
            playerInput = int(input("\t" + O + ", you selected a filled square. Try again. Select a square (1-9):" + "\n"))
        else:
            playerInput
            square[playerInput] # Allocate playerInput to index number on list
            square[playerInput] = "O"
        board()


def winGame():
    if (square[0] != None) and (square[0] == square[1]) and (square[1] == square[2]):
        print("Congratulations! You have won. First row horizontal")
    if (square[3] != None) and (square[3] == square[4]) and (square[4] == square[5]):
        print("Congratulations! You have won. Middle row horizontal")
    if (square[6] != None) and (square[6] == square[7]) and (square[7] == square[8]):
        print("Congratulations! You have won. Last row horizontal")
    if (square[0] != None) and (square[0] == square[3]) and (square[3] == square[6]):
        print("Congratulations! You have won. First row vertical")
    if (square[1] != None) and (square[1] == square[4]) and (square[4] == square[7]):
        print("Congratulations! You have won. Middle row vertical")
    if (square[2] != None) and (square[2] == square[5]) and (square[5] == square[8]):
        print("YCongratulations! You have won. Last row vertical")
    if (square[0] != None) and (square[0] == square[4]) and (square[4] == square[8]):
        print("Congratulations! You have won. Left diagonal")
    if (square[2] != None) and (square[2] == square[4]) and (square[4] == square[6]):
        print("Congratulations! You have won. Right diagonal")


# def endGame():
#     if (square[0] != None) and (square[0] == square[1]) and (square[1] == square[2]);

#     if (square[2] == square[3]) and (square[3] == square[4]) and (square[4] == square[5]) and (square[5] == square[6]) and (square[6] == square[7]) and (square[7] == square[8]):
#         print("Game Over")
addX()
addO()
addX()
addO()
addX()
addO()
addX()
addO()
addX()
winGame()



# clear()
# list.clear()









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




