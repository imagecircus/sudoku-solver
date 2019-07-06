# Sudoku Solver
I had been wondering for a while if I could write a script that would solve sudoku puzzles and I also wanted to learn Python. This is an *attempt* at both.

Currently this project will only solve the **very simplest** form of 9x9 Sudoku puzzles.

# How it works
- Calculates all valid answers for every empty cell
- Looks for cells that only have one valid answer
- Inserts the valid answer and removes the cell(s) from the list of empty cells
- Loops back through the first three steps until all answers have been found
- ... or fails if the number of answers left does not decrease after an iteration

# Example output
```
Puzzle

| |2|8| | | |3|6| |
|5| | |9| |7| | |2|
|1| |4|6| |3|8| |5|
| |8|2|5| |1|7|3| |
| | | | | | | | | |
| |1|7|4| |8|5|2| |
|8| |5|2| |6|9| |3|
|2| | |7| |9| | |6|
| |9|6| | | |2|5| |


Iteration 1

| |2|8|1| | |3|6| |
|5| |3|9| |7| | |2|
|1|7|4|6|2|3|8| |5|
| |8|2|5| |1|7|3| |
| | | |3| |2| | | |
| |1|7|4| |8|5|2|9|
|8| |5|2| |6|9| |3|
|2| | |7| |9| | |6|
| |9|6| | |4|2|5| |


Iteration 2

|9|2|8|1| |5|3|6| |
|5|6|3|9| |7| | |2|
|1|7|4|6|2|3|8|9|5|
| |8|2|5| |1|7|3|4|
| | |9|3| |2| | | |
| |1|7|4|6|8|5|2|9|
|8|4|5|2|1|6|9| |3|
|2| |1|7| |9| | |6|
| |9|6|8| |4|2|5| |


Iteration 3

|9|2|8|1|4|5|3|6|7|
|5|6|3|9| |7| | |2|
|1|7|4|6|2|3|8|9|5|
|6|8|2|5|9|1|7|3|4|
| |5|9|3|7|2| | | |
|3|1|7|4|6|8|5|2|9|
|8|4|5|2|1|6|9|7|3|
|2|3|1|7| |9|4| |6|
| |9|6|8|3|4|2|5| |


Iteration 4

|9|2|8|1|4|5|3|6|7|
|5|6|3|9|8|7|1| |2|
|1|7|4|6|2|3|8|9|5|
|6|8|2|5|9|1|7|3|4|
|4|5|9|3|7|2| | | |
|3|1|7|4|6|8|5|2|9|
|8|4|5|2|1|6|9|7|3|
|2|3|1|7|5|9|4|8|6|
|7|9|6|8|3|4|2|5|1|


Iteration 5

|9|2|8|1|4|5|3|6|7|
|5|6|3|9|8|7|1|4|2|
|1|7|4|6|2|3|8|9|5|
|6|8|2|5|9|1|7|3|4|
|4|5|9|3|7|2|6|1|8|
|3|1|7|4|6|8|5|2|9|
|8|4|5|2|1|6|9|7|3|
|2|3|1|7|5|9|4|8|6|
|7|9|6|8|3|4|2|5|1|


Solved in 0:00:00.028963.
```
