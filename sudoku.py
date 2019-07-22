from clues import clues_for_sudoku_1, clues_for_sudoku_2, clues_for_sudoku_medium, clues_for_sudoku_hard, clues_for_sudoku_expert
from datetime import datetime
from functions import generate_new_puzzle, add_values_to_puzzle, print_the_puzzle, get_empty_cell_locations, get_invalid_answers, get_all_valid_answers, get_box_coordinates, find_cells_with_one_answer, check_boxes_for_unique_values, check_rows_and_cols_for_unique_values, output_puzzle_as_json

# Start a timer
startTime = datetime.now()

# Create a new puzzle with no answers
sudoku = generate_new_puzzle()
sudoku = add_values_to_puzzle(clues_for_sudoku_hard, sudoku)
print("\nStart")
print_the_puzzle(sudoku)

empty_cells = get_empty_cell_locations(sudoku)
print("\nThere are {} answers left to find.".format(len(empty_cells)))

iteration = 1
while len(empty_cells) > 0:
  answers_left_before_iteration = len(empty_cells)

  answers = get_all_valid_answers(sudoku)

  single_answers = find_cells_with_one_answer(answers)
  sudoku = add_values_to_puzzle(single_answers, sudoku)

  unique_values_in_boxes = check_boxes_for_unique_values(answers)
  sudoku = add_values_to_puzzle(unique_values_in_boxes, sudoku)

  unique_answers_in_rows_and_cols = check_rows_and_cols_for_unique_values(answers)
  sudoku = add_values_to_puzzle(unique_answers_in_rows_and_cols, sudoku)

  empty_cells = get_empty_cell_locations(sudoku)

  if len(empty_cells) == answers_left_before_iteration:
    print("\nFAILED after {} iterations in {}".format(iteration, datetime.now() - startTime))
    print("No new answers found. Unable to solve this puzzle.")
    break

  print("\n\n Iteration {}".format(iteration))
  print_the_puzzle(sudoku)
  print("\nThere are {} answers left to find.".format(len(empty_cells)))
  # filename = "iteration-{}".format(iteration)
  # output_puzzle_as_json(sudoku, filename)
  iteration += 1

if len(empty_cells) <= 0:
  print("\nCompleted")
  print_the_puzzle(sudoku)
  print("\nSOLVED in {} iterations in {}".format(iteration, datetime.now() - startTime))
