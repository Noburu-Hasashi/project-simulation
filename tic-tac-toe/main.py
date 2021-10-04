from winning_ai import *
from game import *
import random

def get_input_type():
	while True:
		try:
			player_X_input = int(input('''Enter the number for the type of input for player 'X' :
	1. Asks user for input
	2. Random AI
	3. Winning AI
	: '''))
			if len(str(player_X_input)) != 1:
				raise ValueError
			player_O_input = int(input('''Enter the number for the type of input for player 'O' :
	1. Asks user for input
	2. Random AI
	3. Winning AI
	: '''))
			if len(str(player_O_input)) != 1:
				raise ValueError
		except(ValueError, TypeError, SyntaxError):
			print("- - -ERROR! INVALID INPUT! TRY AGAIN!- - -")
		finally:
			return player_X_input, player_O_input

def get_move_from_input_type(input_type_number, board, player):
	if input_type_number == 1:
		return human_player()
	if input_type_number == 2:
		return random_ai(board, player)
	if input_type_number == 3:
		coordinates = finds_winning_moves_ai(board, player)
		if coordinates == None:
			if player == 'X':
				coordinates = finds_winning_moves_ai(board, 'O')
				if coordinates == None:
					coordinates = random_ai(board, 'X')
			if player == 'O':
				coordinates = finds_winning_moves_ai(board, 'X')
				if coordinates == None:
					coordinates = random_ai(board, 'O')
		return coordinates

board = new_board()  # constructs an empty board

player_X_input, player_O_input = get_input_type()
players = ['X', 'O']  # choses a random player to start the game
current_player = players[random.randint(0, 1)]

print("Player '", current_player, "' goes first!")
render(board)

for turn in range(9):
	if current_player == 'X':
		current_move_type_number = player_X_input
	elif current_player == 'O':
		current_move_type_number = player_O_input
	coordinates = get_move_from_input_type(current_move_type_number, board, current_player)
	make_move(coordinates, board, current_player)
	render(board)
	winner = get_winner(board)
	if winner == None:
		if turn == 8:
			print("- - -GAME ENDED! THIS GAME IS A DRAW!- - -")
			break
	if current_player == 'X':
		current_player = 'O'
	elif current_player == 'O':
		current_player = 'X'
	if winner == 'X':
		print("- - -GAME ENDED! PLAYER 'X' IS THE WINNER!- - -")
		break
	if winner == 'O':
		print("- - -GAME ENDED! PLAYER 'O' IS THE WINNER!- - -")
		break