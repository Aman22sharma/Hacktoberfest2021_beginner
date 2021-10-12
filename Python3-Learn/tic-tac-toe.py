# Tic-Tac-Toe
#create game board
# game board is made up of 3 lists containing 3 elements each
# every element in the list starts out as a blank space, and may gain an "X" or "O" as the user plays the game.
game_over=False
row0 = ["","",""]
row1 = ["","",""]
row2 = ["","",""]
def printBoard(row0,row1,row2):
    global game_over
    print("Current Player: " + currentPlayer)
    print(" -0-1-2-")
    print("0: |" + row0[0] + "|" + row0[1] + "|" + row0[2] + "|")
    print(" -------")
    print("1: |" + row1[0] + "|" + row1[1] + "|" + row1[2] + "|")
    print(" -------")
    print("2: |" + row2[0] + "|" + row2[1] + "|" + row2[2] + "|")
    print(" -------")
    print("")
def checkRows(row0,row1,row2):
    global game_over
    if ((row0[0] == "X") and (row0[1] == "X") and (row0[2] == "X")):
        print("Player X wins in row 0!")
        game_over =True
    if ((row0[0] == "O") and (row0[1] == "O") and (row0[2] == "O")):
        print("Player O wins in row 0!")
        game_over =True
    # row 1
    if ((row1[0] == "X") and (row1[1] == "X") and (row1[2] == "X")):
        print("Player X wins in row 1!")
        game_over =True
    if ((row1[0] == "O") and (row1[1] == "O") and (row1[2] == "O")):
        print("Player O wins in row 1!")
        game_over =True
    # row 2
    if ((row2[0] == "X") and (row2[1] == "X") and (row2[2] == "X")):
        print("Player X wins in row 2!")
        game_over =True
    if ((row2[0] == "O") and (row2[1] == "O") and (row2[2] == "O")):
        print("Player O wins in row 2!")
        game_over =True
def checkCols(row0,row1,row2):
    global game_over
    if ((row0[0] == "X") and (row1[0] == "X") and (row2[0] == "X")):
        print("Player X wins in column 0!")
        game_over =True
    if ((row0[0] == "O") and (row1[0] == "O") and (row2[0] == "O")):
        print("Player O wins in column 0!")
        game_over =True
    # column 1
    if ((row0[1] == "X") and (row1[1] == "X") and (row2[1] == "X")):
        print("Player X wins in column 1!")
        game_over =True
    if ((row0[1] == "O") and (row1[1] == "O") and (row2[1] == "O")):
        print("Player O wins in column 1!")
        game_over =True
    # column 2
    if ((row0[2] == "X") and (row1[2] == "X") and (row2[2] == "X")):
        print("Player X wins in column 2!")
        game_over =True
    if ((row0[2] == "O") and (row1[2] == "O") and (row2[2] == "O")):
        print("Player O wins in column 2!")
def checkDiagonals(row0,row1,row2):
        # first diagonal
    if ((row0[0] == "X") and (row1[1] == "X") and (row2[2] == "X")):
        print("Player X wins in first diagonal!")
        game_over =True
    if ((row0[0] == "O") and (row1[1] == "O") and (row2[2] == "O")):
        print("Player O wins in first diagonal!")
        game_over =True
    # second diagonal
    if ((row0[2] == "X") and (row1[1] == "X") and (row2[0] == "X")):
        print("Player X wins in second diagonal!")
        game_over =True
    if ((row0[2] == "O") and (row1[1] == "O") and (row2[0] == "O")):
        print("Player O wins in secong diagonal!")
# Initialize a current player variable
currentPlayer = input("X or O? ")
# Create a “counter or variable” that should become “True” when the game is over, but remains “False” until it is over
    # print current player turn and game board
    # get row and column for current player
while game_over == False:
    inputRow = int(input("Enter player " + currentPlayer + " row: "))
    inputCol = int(input("Enter player " + currentPlayer + " col: "))
    print("")
    # place mark in appropriate cell
    if (inputRow == 0):
        row0[inputCol] = currentPlayer
    elif (inputRow == 1):
        row1[inputCol] = currentPlayer
    elif (inputRow == 2):
        row2[inputCol] = currentPlayer
    else:
        game_over = True
    # escape from loop on invalid row   
    # Create an “if” block that will change the player.
    if currentPlayer == "O":
        currentPlayer = "X"
    elif currentPlayer == "X":
        currentPlayer = "O"
    printBoard(row0,row1,row2)
    checkRows(row0,row1,row2)
    checkCols(row0,row1,row2)
    checkDiagonals(row0,row1,row2)
    # Check to see if there is 3-in-a-row in any direction.
    # There are 8 possibilities, so write code that will manually check each one for the same marks in a row.
    # If 3 in a row is found, print a winning message and set a variable to “True” to escape loop.
    #The first row and column has been done for you. Complete the remaining rows and columns.
    #Check the diagonals for 3 in a diagonal too. The first one has been done for you.
    # row 0
# After the while loop finishes, print the final board and game-over message. The first one has been done for you. Complete the code for the board.
print(" -0-1-2-")
print("0: |" + row0[0] + "|" + row0[1] + "|" + row0[2] + "|")
print(" -------")
print("1: |" + row1[0] + "|" + row1[1] + "|" + row1[2] + "|")
print("2: |" + row2[0] + "|" + row2[1] + "|" + row2[2] + "|")
print("")
print("GAME OVER")
