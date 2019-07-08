from datetime import datetime
from functions import generate_new_puzzle, print_the_puzzle, get_invalid_answers, get_all_valid_answers, add_clues_to_puzzle, add_answers_to_puzzle, get_empty_cell_locations, get_box_cell_is_in, check_boxes_for_unique_values, find_cells_with_one_answer

startTime = datetime.now()

# Clues for sudoku1.png
clues_for_sudoku_1 = {
	11 : 6,
	15 : 9,
	16 : 7,
	18 : 4,
	19 : 3,
	22 : 5,
	23 : 4,
	25 : 8,
	26 : 6,
	29 : 7,
	32 : 7,
	45 : 1,
	48 : 3,
	49 : 5,
	51 : 5,
	52 : 3,
	54 : 7,
	56 : 9,
	58 : 8,
	59 : 6,
	61 : 4,
	62 : 2,
	65 : 6,
	78 : 9,
	81 : 2,
	84 : 9,
	85 : 7,
	87 : 6,
	88 : 5,
	91 : 7,
	92 : 9,
	94 : 8,
	95 : 4,
	99 : 2,
}
# Clues for sudoku1.png
clues_for_sudoku_2 = {
	12 : 2,
	13 : 8,
	17 : 3,
	18 : 6,
	21 : 5,
	24 : 9,
	26 : 7,
	29 : 2,
	31 : 1,
	33 : 4,
	34 : 6,
	36 : 3,
	37 : 8,
	39 : 5,
	42 : 8,
	43 : 2,
	44 : 5,
	46 : 1,
	47 : 7,
	48 : 3,
	62 : 1,
	63 : 7,
	64 : 4,
	66 : 8,
	67 : 5,
	68 : 2,
	71 : 8,
	73 : 5,
	74 : 2,
	76 : 6,
	77 : 9,
	79 : 3,
	81 : 2,
	84 : 7,
	86 : 9,
	89 : 6,
	92 : 9,
	93 : 6,
	97 : 2,
	98 : 5,
}
# Clues for Puzzle 384
clues_for_Puzzle384 = {
	11 : 1,
	16 : 3,
	19 : 4,
	21 : 6,
	24 : 1,
	26 : 4,
	27 : 7,
	32 : 8,
	44 : 5,
	53 : 1,
	55 : 2,
	58 : 6,
	59 : 8,
	63 : 9,
	66 : 6,
	68 : 4,
	74 : 2,
	75 : 7,
	77 : 5,
	81 : 5,
	89 : 1,
	92 : 7,
}
# Clues for Puzzle 384
clues_for_Puzzle356 = {
	15 : 8,
	17 : 3,
	18 : 7,
	24 : 7,
	37 : 6,
	39 : 5,
	42 : 7,
	46 : 4,
	49 : 1,
	51 : 1,
	54 : 2,
	55 : 7,
	57 : 8,
	61 : 9,
	64 : 6,
	72 : 4,
	73 : 2,
	74 : 3,
	78 : 9,
	81 : 7,
	82 : 1,
	85 : 6,
	87 : 4,
	92 : 6,
	97 : 2,
	98 : 3
}

# Create a dictionary of all the co-ordinates with no values
sudoku = generate_new_puzzle()

# Add a set of clues to the puzzle
sudoku = add_clues_to_puzzle(clues_for_Puzzle356, sudoku)

# Gerenate a list of all the empty cells in the puzzle
empty_cells = get_empty_cell_locations(sudoku)

# Print the puzzle
print()
print("Puzzle")
print_the_puzzle(sudoku)

# create a placeholder to store the potential solutions
all_valid_answers = {}

i = 1
while len(empty_cells) > 0:

	answers_left_before_iteration = len(empty_cells)
	print("There are {} answers left to find \n\n".format(answers_left_before_iteration))

	all_valid_answers = get_all_valid_answers(sudoku)

	# find all cells with only one valid answer
	# input the answers and update list of empty_cells
	single_answers = find_cells_with_one_answer(all_valid_answers)
	add_answers_to_puzzle(single_answers, sudoku)
	empty_cells = get_empty_cell_locations(sudoku)

	# find all unique values within every box
	# input the answers and update list of empty_cells
	unique_values_in_box = check_boxes_for_unique_values(all_valid_answers)
	add_answers_to_puzzle(unique_values_in_box, sudoku)
	empty_cells = get_empty_cell_locations(sudoku)

	# if no answers are found print an error and escape the loop
	if len(empty_cells) == answers_left_before_iteration:
		print("FAILED: No certain answers left")
		break

	print()
	print("Iteration {}".format(i))
	print_the_puzzle(sudoku)

	i += 1

# when no answers are left to be found print solved and how long it took
if len(empty_cells) <= 0:
	print("")
	print("Solved in {}.\n".format(datetime.now() - startTime))
