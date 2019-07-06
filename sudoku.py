from datetime import datetime
from functions import generate_new_game, print_the_puzzle, get_invalid_answers, add_clues_to_game, get_answer_cell_locations, get_box_cell_is_in

startTime = datetime.now()

answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a dictionary of all the co-ordinates with no values
sudoku = generate_new_game()

# Add the clues for sudoku1.png
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

# Add the clues for sudoku1.png
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


sudoku = add_clues_to_game(clues_for_Puzzle356, sudoku)
answer_cells = get_answer_cell_locations(clues_for_Puzzle356, sudoku)

# Print the puzzle
print()
print("Puzzle")
print_the_puzzle(sudoku)

# create a placeholder to store the potential solutions
potential_solutions = {}

i = 1
while len(answer_cells) > 0:
	# clear the dictionary and list to iterate again
	potential_solutions.clear()
	potential_answers = []
	invalid_answers = []
	answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	answers_left_before_iteration = len(answer_cells)

	for cell in answer_cells:
		invalid_answers = get_invalid_answers(cell, sudoku)
		potential_answers = set(answers) - set(invalid_answers)
		potential_answers = list(potential_answers)
		potential_solutions.update({cell: potential_answers})

	for location, answers in potential_solutions.items():
		if len(answers) == 1:
			sudoku.update({location : answers[0]})
			answer_cells.remove(location)

	if len(answer_cells) == answers_left_before_iteration:
		print("FAILED: No certain answers left")
		break

	print()
	print("Iteration {}".format(i))
	print_the_puzzle(sudoku)

	i += 1

if len(answer_cells) <= 0:
	print("")
	print("Solved in {}.\n".format(datetime.now() - startTime))
