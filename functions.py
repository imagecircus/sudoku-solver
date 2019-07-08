
# Create a dictionary of all the co-ordinates with no values
def generate_new_puzzle():
	skips = [20, 30, 40, 50, 60, 70, 80, 90]
	i = 11
	puzzle = {}
	while i<=99:
		if i in skips:
			i += 1
			continue
		puzzle.update({ i : ""})
		i += 1
	return puzzle

# add the clues the empty sudoku game
def add_clues_to_puzzle(clues, puzzle):
	for location, value in clues.items():
		puzzle[location] = value
	return puzzle

# get a list of the locations of the cells that are empty
def get_empty_cell_locations(puzzle):
  empty_cells = []
  for location, value in puzzle.items():
    if value == "":
      empty_cells.append(location)
    else:
      continue
  return empty_cells


def get_all_valid_answers(puzzle):
  empty_cells = get_empty_cell_locations(puzzle)
  # create a placeholder to store the potential solutions
  all_valid_answers = {}

  # make sure the dictionary and lists are clear to start the iteration
  all_valid_answers.clear()
  cell_answers = []
  invalid_answers = []
  answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  # find all valid answers for all empty cells
  for cell in empty_cells:
  	invalid_answers = get_invalid_answers(cell, puzzle)
  	cell_answers = list(set(answers) - set(invalid_answers))
  	all_valid_answers.update({cell: cell_answers})
  return all_valid_answers

def add_answers_to_puzzle(answers, puzzle):
	for location, answer in answers.items():
		puzzle.update({location : answer[0]})


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

def find_cells_with_one_answer(answers):
  single_answers = {}
  for location, answers in answers.items():
    if len(answers) == 1:
      single_answers.update({location : answers})
  return single_answers

# check within potential answers for each box for values that only appear once
# return a dictionary of unique values and their locations
def check_boxes_for_unique_values(potential_answers):
	boxes = []
	box_1 = [11, 12, 13, 21, 22, 23, 31, 32, 33]
	box_2 = [14, 15, 16, 24, 25, 26, 34, 35, 36]
	box_3 = [17, 18, 19, 27, 28, 29, 37, 38, 39]
	box_4 = [41, 42, 43, 51, 52, 53, 61, 62, 63]
	box_5 = [44, 45, 46, 54, 55, 56, 64, 65, 66]
	box_6 = [47, 48, 49, 57, 58, 59, 67, 68, 69]
	box_7 = [71, 72, 73, 81, 82, 83, 91, 92, 93]
	box_8 = [74, 75, 76, 84, 85, 86, 94, 95, 96]
	box_9 = [77, 78, 79, 87, 88, 89, 97, 98, 99]
	boxes += [box_1]
	boxes += [box_2]
	boxes += [box_3]
	boxes += [box_4]
	boxes += [box_5]
	boxes += [box_6]
	boxes += [box_7]
	boxes += [box_8]
	boxes += [box_9]

	output = {}
	for box in boxes:
		this_box = {}
		keys_to_remove = []
		values_to_remove = []

		# Create a dictionary of all the potential answers in a box
		for location in box:
			if location in potential_answers:
				this_box.update({location : potential_answers.get(location)})

		# Remove any potential answers that are a single value (definite answer)
		# but store the value
		for location, value in this_box.items():
			if len(value) == 1:
				keys_to_remove.append(location)
				values_to_remove.append(value[0])
		for key in keys_to_remove:
			this_box.pop(key)

		# Loop though all remaining values removing and known values from lists
		# of answers
		for location, value in this_box.items():
			for number in value:
				if number in values_to_remove:
					this_box[location].remove(number)

		# Create a dictionary of all the locations and values for definite answers
		# within boxes
		for location, value in this_box.items():
			if len(value) == 1:
				output.update({location : value})
	return output
	# NOTE:
	# This function is not actually doing what it was intended to. While it does
	# make the script solve puzzles faster and in fewer iterations, it is not
	# actually looking for unique values within the box. Some of the logic
	# from here should probably move into a different function and this should
	# be rewritten to achieve its purpose.
