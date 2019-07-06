# Create a dictionary of all the co-ordinates with no values
def generate_new_game():
	skips = [20, 30, 40, 50, 60, 70, 80, 90]
	i = 11
	game = {}
	while i<=99:
		if i in skips:
			i += 1
			continue
		game.update({ i : ""})
		i += 1
	return game

# add the clues the empty sudoku game
def add_clues_to_game(clues, game):
	for location, value in clues.items():
		game[location] = value
	return game

# get a list of the locations of the cells that are initally blank
def get_answer_cell_locations(clues, game):
	answer_cells = []
	for location, value in game.items():
		if location in clues:
			continue
		else:
			answer_cells.append(location)

	return answer_cells

# print the full puzzle to the command line
def print_the_puzzle(puzzle):
	row_1 = "|"
	row_2 = "|"
	row_3 = "|"
	row_4 = "|"
	row_5 = "|"
	row_6 = "|"
	row_7 = "|"
	row_8 = "|"
	row_9 = "|"

	for location, value in puzzle.items():
		if location <= 19:
			if value is "":
				row_1 += " |"
			else:
				row_1 += str(value) + "|"
		elif location <= 29:
			if value is "":
				row_2 += " |"
			else:
				row_2 += str(value) + "|"
		elif location <= 39:
			if value is "":
				row_3 += " |"
			else:
				row_3 += str(value) + "|"
		elif location <= 49:
			if value is "":
				row_4 += " |"
			else:
				row_4 += str(value) + "|"
		elif location <= 59:
			if value is "":
				row_5 += " |"
			else:
				row_5 += str(value) + "|"
		elif location <= 69:
			if value is "":
				row_6 += " |"
			else:
				row_6 += str(value) + "|"
		elif location <= 79:
			if value is "":
				row_7 += " |"
			else:
				row_7 += str(value) + "|"
		elif location <= 89:
			if value is "":
				row_8 += " |"
			else:
				row_8 += str(value) + "|"
		elif location <= 99:
			if value is "":
				row_9 += " |"
			else:
				row_9 += str(value) + "|"

	print("")
	print(row_1)
	print(row_2)
	print(row_3)
	print(row_4)
	print(row_5)
	print(row_6)
	print(row_7)
	print(row_8)
	print(row_9)
	print()

# return the list of known invalid answers for the given cell
def get_invalid_answers(cell, game):

	row = []
	col = []
	box = []
	cells_in_box = get_box_cell_is_in(cell, game)

	for location, value in game.items():
		# use the first co-ordinate to get all the values for the row the cell is in
		if int(str(location)[0]) == int(str(cell)[0]):
			row.append(value)
		# use the second co-ordinate to get all the values for the column the cell is in
		if int(str(location)[1]) == int(str(cell)[1]):
			col.append(value)
		if location in cells_in_box:
			box.append(value)

	used_values = []
	used_values = row + col + box
	used_values = list(dict.fromkeys(used_values))
	used_values.remove("")
	used_values.sort()
	return used_values

# return the list of known invalid answers for the given cell
def get_box_cell_is_in(cell, game):

	box = []
	box_1 = [11, 12, 13, 21, 22, 23, 31, 32, 33]
	box_2 = [14, 15, 16, 24, 25, 26, 34, 35, 36]
	box_3 = [17, 18, 19, 27, 28, 29, 37, 38, 39]
	box_4 = [41, 42, 43, 51, 52, 53, 61, 62, 63]
	box_5 = [44, 45, 46, 54, 55, 56, 64, 65, 66]
	box_6 = [47, 48, 49, 57, 58, 59, 67, 68, 69]
	box_7 = [71, 72, 73, 81, 82, 83, 91, 92, 93]
	box_8 = [74, 75, 76, 84, 85, 86, 94, 95, 96]
	box_9 = [77, 78, 79, 87, 88, 89, 97, 98, 99]

	# somehow figure out which box the cell is in - THIS IS BROKEN AS IT RETURNS THE VALUE OF THE CHOSEN CELL WHICH MAKES EVERYTHING BREAK!
	if int(str(cell)[0]) <= 3:
		# then it's in the first column of boxes
		if int(str(cell)[1]) <= 3:
			# then it's in box_1
			if cell in box_1:
				selected_box = box_1
		elif int(str(cell)[1]) <= 6:
			# then it's in box_2
			if cell in box_2:
				selected_box = box_2
		elif int(str(cell)[1]) > 6:
			# then it's in box_3
			if cell in box_3:
				selected_box = box_3
	elif int(str(cell)[0]) <= 6:
		# then it's in the middle column of boxes
		if int(str(cell)[1]) <= 3:
			# then it's in box_4
			if cell in box_4:
				selected_box = box_4
		elif int(str(cell)[1]) <= 6:
			# then it's in box_5
			if cell in box_5:
				selected_box = box_5
		elif int(str(cell)[1]) > 6:
			# then it's in box_6
			if cell in box_6:
				selected_box = box_6
	elif int(str(cell)[0]) > 6:
		# then it's in the final column of boxes
		if int(str(cell)[1]) <= 3:
			# then it's in box_7
			if cell in box_7:
				selected_box = box_7
		elif int(str(cell)[1]) <= 6:
			# then it's in box_8
			if cell in box_8:
				selected_box = box_8
		elif int(str(cell)[1]) > 6:
			# then it's in box_9
			if cell in box_9:
				selected_box = box_9

	return selected_box
