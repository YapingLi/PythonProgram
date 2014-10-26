from random import randint

# Initialize ship board
board = []
for i in range(5):
	board.append(['O'] * 5)

# Print board status
def print_board(board):
	for row in board:
		print "  ".join(row)

# Hide the ship
ship_row = randint(0, len(board) - 1)
ship_column = randint(0, len(board) - 1)

# Seek the ship
def guess_row(): 
	return int(raw_input("Guess row: "))

def guess_column():
	return int(raw_input("Guess column: "))

count = 2
while count >= 0:
	guessed_row = guess_row()
	guessed_column = guess_column()
	count -= 1
	if guessed_row == ship_row and guessed_column == ship_column:
		print "Congratulations! You sunk my battleship!"
	else:
		if guessed_row >= len(board) or guessed_row < 0:
			print "Oops, you are not even in the ocean! Row needs to be >= 0 & <", len(board), "! Please try again. "
		elif guessed_column >= len(board) or guessed_column < 0:
			print "Oops, you are not even in the ocean! Column needs to be >= 0 & <", len(board), "! Please try again. "
		elif guessed_row != ship_row or guessed_column != ship_column:
			if board[guessed_row][guessed_column] != 'X':
				board[guessed_row][guessed_column] = 'X'
				print "You missed my battleship! Pleae try again."
			else:
				print "Remember? You've guessed that one already. Please try again."
			print_board
		
		


