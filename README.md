# Sudoku Solver
I had been wondering for a while if I could write a script that would solve sudoku puzzles and I also wanted to learn Python. This is an *attempt* at both.

Currently this project will only solve the **very simplest** form of 9x9 Sudoku puzzles.

# How it works
- Calculates all valid answers for every empty cell
- Looks for cells that only have one valid answer
- Inserts the valid answer and removes the cell(s) from the list of empty cells
- Loops back through the first three steps until all answers have been found
- ... or fails if the number of answers left does not decrease after an iteration
