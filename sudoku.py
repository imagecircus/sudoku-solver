from clues import clues_for_sudoku_1, clues_for_sudoku_2, clues_for_Puzzle356, clues_for_Puzzle384, clues_for_Sudoku_Medium, clues_for_Sudoku_Hard, clues_for_Sudoku_Expert
from datetime import datetime
from functions import generate_new_puzzle, print_the_puzzle, get_invalid_answers, get_all_valid_answers, add_clues_to_puzzle, add_answers_to_puzzle, get_empty_cell_locations, get_box_cell_is_in, check_boxes_for_unique_values, find_cells_with_one_answer, output_puzzle_as_json, check_rows_and_cols_for_unique_values

# Start a timer
startTime = datetime.now()

# Create a dictionary of all the co-ordinates with no values
sudoku = generate_new_puzzle()

# Add a set of clues to the puzzle - imported from clues.py in line 1
sudoku = add_clues_to_puzzle(clues_for_Sudoku_Hard, sudoku)

# Gerenate a list of all the empty cells in the puzzle
empty_cells = get_empty_cell_locations(sudoku)

# Print the puzzle in its initial state
print()
print("Puzzle")
print_the_puzzle(sudoku)

# create a placeholder to store all the valid answers
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

	unique_answers_in_rows_and_cols = check_rows_and_cols_for_unique_values(all_valid_answers)
	add_answers_to_puzzle(unique_answers_in_rows_and_cols, sudoku)
	empty_cells = get_empty_cell_locations(sudoku)

	# if no answers are found print an error and escape the loop
	if len(empty_cells) == answers_left_before_iteration:
		print("FAILED: No certain answers left")
		break

	print()
	print("Iteration {}".format(i))
	print_the_puzzle(sudoku)
	filename = "iteration_" + str(i)
#	output_puzzle_as_json(sudoku, filename)
	i += 1

# when no answers are left to be found print solved and how long it took
if len(empty_cells) <= 0:
	print("")
	print("Solved in {}.\n".format(datetime.now() - startTime))
