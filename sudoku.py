from clues import *
from datetime import datetime
from functions import (
  generate_new_puzzle,
  add_values_to_puzzle,
  print_the_puzzle,
  get_empty_cell_locations,
  get_all_valid_answers,
  find_cells_with_one_answer,
  check_boxes_for_unique_values,
  check_rows_and_cols_for_unique_values,
  output_puzzle_as_json,
)

# Start a timer
startTime = datetime.now()

# Create a new puzzle with no answers
sudoku = generate_new_puzzle()
sudoku = add_values_to_puzzle(clues_for_sudoku_hard, sudoku)
print("\nStart")
print_the_puzzle(sudoku)

# Check for locations of empty cells and print a message to say how many there are.
empty_cells = get_empty_cell_locations(sudoku)
print("\nThere are {} answers left to find.".format(len(empty_cells)))

# Start iterating through methods of solving the puzzle
iteration = 0
while len(empty_cells) > 0:
  iteration += 1
  answers_left_before_iteration = len(empty_cells)

  # Find all valid answers for all of the empty cells
  answers = get_all_valid_answers(sudoku)

  # Find all cells that only have one valid answer and input them
  single_answers = find_cells_with_one_answer(answers)
  sudoku = add_values_to_puzzle(single_answers, sudoku)

  # Find any values that only appear once in a box and input them
  unique_values_in_boxes = check_boxes_for_unique_values(answers)
  sudoku = add_values_to_puzzle(unique_values_in_boxes, sudoku)

  # Find any values that only appear once in any row or column and input them
  unique_answers_in_rows_and_cols = check_rows_and_cols_for_unique_values(answers)
  sudoku = add_values_to_puzzle(unique_answers_in_rows_and_cols, sudoku)

  # Update the list of empty cells
  empty_cells = get_empty_cell_locations(sudoku)

  # If the amount of empty cells didn't decrease this iteration stop itrerating and display an error
  if len(empty_cells) == answers_left_before_iteration:
    print("\nFAILED after {} iterations in {}".format(iteration, datetime.now() - startTime))
    print("No new answers found. Unable to solve this puzzle.")
    break

  # Print the latest iteration of the puzzle and how many answers are left to find.
  print("\n\n Iteration {}".format(iteration))
  print_the_puzzle(sudoku)
  print("\nThere are {} answers left to find.".format(len(empty_cells)))

  # Output each iteration of the puzzle as a separate JSON file
  # filename = "iteration-{}".format(iteration)
  # output_puzzle_as_json(sudoku, filename)

# If there are no more answers to solve then print the solved puzzle and the time it took
if len(empty_cells) <= 0:
  print("\nCompleted")
  print_the_puzzle(sudoku)
  print("\nSOLVED in {} iterations in {}".format(iteration, datetime.now() - startTime))
