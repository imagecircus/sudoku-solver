# Steps to solve a sudoku puzzle
- [x] find all empty cells - `get_empty_cell_locations(puzzle)`
- [x] find all answers for all empty cells - `get_all_valid_answers(puzzle)`
- [x] check for cells that only have one answer - `find_cells_with_one_answer(answers)`
- [x] input answer into grid - `input_answers(puzzle, answers)`
- [ ] remove values used from any potential answers across relevant box, row and column
- [x] ~~remove answered cells from the list of potential answers~~ - `get_empty_cell_locations(puzzle)`
- [ ] check within the potential answers for each box for any value that only appears once
  - [x] input answer into grid - `input_answers(puzzle, answers)`
  - [ ] remove answered cells from the list of potential answers

- [x] loop until all answers are found
  - [x] stop and show an error if no new answers are found in an iteration
