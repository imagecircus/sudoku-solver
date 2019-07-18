from collections import Counter
import json

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

# return a dictionary containing each cell location and all valid answers
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

# add a dictionary of answers into the puzzle
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

# dump the puzzle into a JSON file with the name filename.json
def output_puzzle_as_json(puzzle, filename):
	the_filename = filename + ".json"
	with open(the_filename, 'w') as json_file:
	  json.dump(puzzle, json_file)

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

# return a dictionary of cell locations and answers for cells with only one answer
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
	i = 0
	output = {}
	for box in boxes:
		this_box = {}
		keys_to_remove = []
		all_values = []
		i += 1
		# Create a dictionary of all the potential answers in a box
		for location in box:
			if location in potential_answers:
				this_box.update({location : potential_answers.get(location)})

		# create a list of all possible answers in the box
		for location, values in this_box.items():
			for value in values:
				all_values.append(value)

		# check the list for values that appear only once within the box
		# output a dictionary of the locations and values of unique answers
		for value, count in Counter(all_values).most_common():
			if count == 1:
				unique_answer = ""
				unique_answer = value
				for location, values in this_box.items():
					for value in values:
						if value == unique_answer:
							output.update({location : [value]})

	return output

# return a dictionary of locations and answers for answers that only appear once in a row or col
def check_rows_and_cols_for_unique_values(answers):
	rows = {}
	cols = {}
	output = {}
	i = 1
	while i <= 9:
		rows.update({"row {}".format(i) : {}})
		cols.update({"col {}".format(i) : {}})
		i += 1

	for location, value in answers.items():

		# use the first co-ordinate to get all the values for the row the cell is in
		if int(str(location)[0]) == 1:
			rows["row 1"][str(location)] = value
		elif int(str(location)[0]) == 2:
			rows["row 2"][str(location)] = value
		elif int(str(location)[0]) == 3:
			rows["row 3"][str(location)] = value
		elif int(str(location)[0]) == 4:
			rows["row 4"][str(location)] = value
		elif int(str(location)[0]) == 5:
			rows["row 5"][str(location)] = value
		elif int(str(location)[0]) == 6:
			rows["row 6"][str(location)] = value
		elif int(str(location)[0]) == 7:
			rows["row 7"][str(location)] = value
		elif int(str(location)[0]) == 8:
			rows["row 8"][str(location)] = value
		elif int(str(location)[0]) == 9:
			rows["row 9"][str(location)] = value

		# use the second co-ordinate to get all the values for the column the cell is in
		if int(str(location)[1]) == 1:
			cols["col 1"][str(location)] = value
		elif int(str(location)[1]) == 2:
			cols["col 2"][str(location)] = value
		elif int(str(location)[1]) == 3:
			cols["col 3"][str(location)] = value
		elif int(str(location)[1]) == 4:
			cols["col 4"][str(location)] = value
		elif int(str(location)[1]) == 5:
			cols["col 5"][str(location)] = value
		elif int(str(location)[1]) == 6:
			cols["col 6"][str(location)] = value
		elif int(str(location)[1]) == 7:
			cols["col 7"][str(location)] = value
		elif int(str(location)[1]) == 8:
			cols["col 8"][str(location)] = value
		elif int(str(location)[1]) == 9:
			cols["col 9"][str(location)] = value

	for row, answers in rows.items():
		all_values = []
		for location, values in answers.items():
			for value in values:
				all_values.append(value)

		for value, count in Counter(all_values).most_common():
			if count == 1:
				for location, values in answers.items():
					for single_value in values:
						if single_value == value:
							output.update({ int(location) : [value]})

	for col, answers in cols.items():
		all_values = []
		for location, values in answers.items():
			for value in values:
				all_values.append(value)

		for value, count in Counter(all_values).most_common():
			if count == 1:
				for location, values in answers.items():
					for single_value in values:
						if single_value == value:
							output.update({ int(location) : [value]})

	return output
