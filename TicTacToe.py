# import random module
import random

# initialize empty board
board = [" "," "," "," "," "," "," "," "," ",]

# opens/creates a log file in append mode
f = open("TicTacToe-LogFile.txt", "a")

# function to display game board
def showBoard():
	print(board[0], "|", board[1], "|", board[2])
	print("--+---+--")
	print(board[3], "|", board[4], "|", board[5])
	print("--+---+--")
	print(board[6], "|", board[7], "|", board[8])
	print()

# function that asks player whether to play as X or O
def playAs():
	
	symbol = input("Do you want to play as \'X\' or \'O\'?: ").upper()
	
	# prevent user entering invalid input
	while symbol != "X" and symbol != "O":
		print("INVALID INPUT: Please enter either \'X\' or \'O\'")
		symbol = input("Play as: ").upper()

	# announce human player's symbol
	print("\nYou are now playing as", symbol, "\n")

	# assign symbol to player
	global Human, Computer
	if symbol == "X":
		Human = "X"
		Computer = "O"
	else:
		Human = "O"
		Computer = "X"

# converts row and column of board to its corresponding list index
def convRCtoIndex(row, column):
	if row == 1 and column == 1:
		return 0
	elif row == 1 and column == 2:
		return 1
	elif row == 1 and column == 3:
		return 2
	elif row == 2 and column == 1:
		return 3
	elif row == 2 and column == 2:
		return 4
	elif row == 2 and column == 3:
		return 5
	elif row == 3 and column == 1:
		return 6
	elif row == 3 and column == 2:
		return 7
	elif row == 3 and column == 3:
		return 8

# function that converts index of board to corresponding row or column value
def convIndextoRC(i, outType):	# i = index, outType = "R"/"C"
	if (i == 0 or i == 3 or i == 6) and outType == "C":
		return 1
	elif (i == 1 or i == 4 or i == 7) and outType == "C":
		return 2
	elif (i == 2 or i == 5 or i == 8) and outType == "C":
		return 3
	elif (i == 0 or i == 1 or i == 2) and outType == "R":
		return 1
	elif (i == 3 or i == 4 or i == 5) and outType == "R":
		return 2
	elif (i == 6 or i == 7 or i == 8) and outType == "R":
		return 3

# function that prompts human player to make a move
def humanMove():
	# announces human player's turn
	if round == 1:
		print(Human, "will make the first move!")
	else:
		print("It's " + str(Human) + "'s turn!")

	# prompts user to make a move
	print("Input the row and column of which you wish to mark", Human, "on")

	row	= int(input("Row: "))  # user enters row number
	while row not in range(1,4):  # prevents user from entering out of range number
		print("INVALID INPUT: Please enter a number between 1 and 3")
		row = int(input("Row: "))

	column = int(input("Column: "))  # user enters row number
	while column not in range(1, 4):  # prevents user from entering out of range number
		print("INVALID INPUT: Please enter a number between 1 and 3")
		column = int(input("Column: "))

	# prevents player from overwriting already occupied spots on the board
	if board[convRCtoIndex(row, column)] != " ": # checks if spot on board is occupied
		print("ERROR: Row", row, "Column", column, "is occupied by", board[convRCtoIndex(row, column)])

		# loop forcing player to pick empty spot on the game board
		while board[convRCtoIndex(row, column)] != " ":
			print("Input the row and column of which you wish to mark", Human, "on")
			row = int(input("Row: "))
			while row not in range(1, 4):  # input validation
				print("INVALID INPUT: Please enter a number between 1 and 3")
				row = int(input("Row: "))
			column = int(input("Column: "))
			while column not in range(1, 4):  # input validation
				print("INVALID INPUT: Please enter a number between 1 and 3")
				column = int(input("Column: "))
	
	# writes an entry into the log file for human player
	f.write(str(round) + ", H, " + str(row) + ", " + str(column) + ", " + str(Human) + "\n")

	# places X/O on the board
	board[convRCtoIndex(row, column)] = Human

	print()  # prints newline

# function that makes computer player's moves
def computerMove():
	# announces computer player's turn
	if round == 1:
		print(Computer, "will make the first move!\n")
	else:
		print("It's " + str(Computer) + "'s turn!\n")

	# computer player places its piece in an empty spot
	searchComplete = False  # variable determining empty spot is found

	while searchComplete == False:  # loops when empty spot is not found
		randSpot = random.randint(0,8)
		if board[randSpot] == " ":  # executes when the a random spot on the board is empty
			board[randSpot] = str(Computer)  # places piece
			searchComplete = True  # empty spot is found, loop ends
	
	# writes an entry into the log file for computer player
	f.write(str(round) + ", C, " + str(convIndextoRC(randSpot, "R")) + ", " + str(convIndextoRC(randSpot, "C")) + ", " + str(Computer) + "\n")

# function to check if human/computer player wins or round draw
def checkWin():
	global GameOver
	# Check if any row has winning set
	if board[0] == board[1] == board[2] and board[2] != " ":
		print(board[2], "wins!")
		GameOver = True
	elif board[3] == board[4] == board[5] and board[5] != " ":
		print(board[5], "wins!")
		GameOver = True
	elif board[6] == board[7] == board[8] and board[8] != " ":
		print(board[8], "wins!")
		GameOver = True
		
	# Check if any column have winning set
	if board[0] == board[3] == board[6] and board[6] != " ":
		print(board[6], "wins!")
		GameOver = True
	elif board[1] == board[4] == board[7] and board[7] != " ":
		print(board[7], "wins!")
		GameOver = True
	elif board[2] == board[5] == board[8] and board[8] != " ":
		print(board[8], "wins!")
		GameOver = True
		
	# Check if any diagonals have winning set
	if board[0] == board[4] == board[8] and board[8] != " ":
		print(board[8], "wins!")
		GameOver = True
	elif board[2] == board[4] == board[6] and board[6] != " ":
		print(board[6], "wins!")
		GameOver = True
	
	# Check if round is draw
	if board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] and board[8] != " " and GameOver != True:
		print("Draw! Nobody wins!")
		GameOver = True
	

restart = True
while restart == True:
    
	# print logo and creator credit
	print("""
 _____ _                _____                     _____           
/__   (_) ___          /__   \__ _  ___          /__   \___   ___ 
  / /\/ |/ __|  _____    / /\/ _` |/ __|  _____    / /\/ _ \ / _ \ 
 / /  | | (__  |_____|  / / | (_| | (__  |_____|  / / | (_) |  __/
 \/   |_|\___|          \/   \__,_|\___|          \/   \___/ \___|
        """)
	print("by Kaviraj Vijayanthiran\n")

	# welcome message
	print("Welcome to a classic game of Tic-Tac-Toe! You will be playing against a computer player\n")

	playAs()

	# randomly decide which player moves on odd rounds
	moveOnOdd = ["H","C"]
	moveOnOdd = moveOnOdd.pop(random.randint(0,1))

	# game begin
	board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]	# resets board
	round = 1	# reset round count to 1
	showBoard()	# shows empty board at begining of rounds
	GameOver = False
	while GameOver == False:	# loops round if game not over
	
		if moveOnOdd == "H":	# Runs when human player makes the first move
			if round % 2 == 1:	# Human's turn
				humanMove()
				showBoard()
				checkWin()
				round += 1
			else:				# Computer's turn
				computerMove()
				showBoard()
				checkWin()
				round += 1
		else:					# Runs when computer player makes the first move
			if round % 2 == 1:	# Computer's turn
				computerMove()
				showBoard()
				checkWin()
				round += 1
			else:				# Human's turn
				humanMove()
				showBoard()
				checkWin()
				round += 1
    
	restart = input("Do you want to replay the game? (Y/N): ").upper()
	while restart != "Y" and restart != "N":
		print("ERROR: Invalid input!")
		restart = input("Do you want to replay the game? Please enter \'Y\' or \'N\': ").upper()
		
	if restart == "Y":
		restart = True
	else:
		restart = False
	f.write("\n")

f.close()
