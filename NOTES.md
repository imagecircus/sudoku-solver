# Steps to solve a sudoku puzzle
- [ ] find all empty cells - `get_empty_cell_locations(puzzle)`
- [ ] find all answers for all empty cells - `get_all_valid_answers(puzzle)`
- [ ] check for cells that only have one answer - `find_cells_with_one_answer(answers)`
- [ ] input answer into grid - `input_answers(puzzle, answers)`
- [ ] remove values used from any potential answers across relevant box, row and column
- [ ] remove answered cells from the list of potential answers
- [ ] check within the potential answers for each box for any value that only appears once
  - [ ] input answer into grid
  - [ ] remove answered cells from the list of potential answers

- [ ] loop until all answers are found
  - [ ] stop and show an error if no new answers are found in an iteration
