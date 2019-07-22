# Sudoku Solver
I had been wondering for a while if I could write a script that would solve sudoku puzzles and I also wanted to learn Python. This is an *attempt* at both.

## So what does it do right now?
Currently this project runs on the command line `python3 sudoku.py` and it will only solve fairly simple 9x9 Sudoku puzzles.

## How does it work?
- Makes a list of all the cells that are empty
- Calculates all valid answers for every empty cell
- Looks for cells that only have one valid answer
- Looks for answers that only have one valid position within a 3x3 box
- Looks for answers that only have one valid position in a row or column
- Inserts the valid answers
- Loops back through the first five steps until all answers have been found
- ... or fails if the number of answers left does not decrease after an iteration

## How is the puzzle stored?
The puzzle is stored as a list of lists Like this:

```
[
  [9, 4, 6, 1, 7, 8, 5, 3, 2],
  [7, 3, 2, 5, 4, 9, 1, 8, 6],
  [5, 1, 8, 6, 2, 3, 4, 7, 9],
  [6, 2, 1, 4, 8, 7, 9, 5, 3],
  [4, 5, 7, 3, 9, 1, 2, 6, 8],
  [3, 8, 9, 2, 5, 6, 7, 1, 4],
  [2, 6, 4, 8, 1, 5, 3, 9, 7],
  [1, 9, 3, 7, 6, 4, 8, 2, 5],
  [8, 7, 5, 9, 3, 2, 6, 4, 1]
]
```

This allows you to retrieve a value by passing in row and column coordinates like `puzzle[2][6]` which in the example above returns `4`.

```
    0   1   2   3   4   5   6   7   8
0 |0,0|0,1|0,2|0,3|0,4|0,5|0,6|0,7|0,8|
1 |1,0|1,1|1,2|1,3|1,4|1,5|1,6|1,7|1,8|
2 |2,0|2,1|2,2|2,3|2,4|2,5|2,6|2,7|2,8|
3 |3,0|3,1|3,2|3,3|3,4|3,5|3,6|3,7|3,8|
4 |4,0|4,1|4,2|4,3|4,4|4,5|4,6|4,7|4,8|
5 |5,0|5,1|5,2|5,3|5,4|5,5|5,6|5,7|5,8|
6 |6,0|6,1|6,2|6,3|6,4|6,5|6,6|6,7|6,8|
7 |7,0|7,1|7,2|7,3|7,4|7,5|7,6|7,7|7,8|
8 |8,0|8,1|8,2|8,3|8,4|8,5|8,6|8,7|8,8|
```


## Example output
```
Start

|5|9| |7| |2| |1|6|
|8| | | | | | | |9|
| | | |5|8|9| | | |
| |5| |8| |6| |2| |
| | | | | | | | | |
| |1| |9| |3| |7| |
| | | |6|2|4| | | |
|1| | | | | | | |5|
|4|3| |1| |5| |6|8|

There are 51 answers left to find.


 Iteration 1

|5|9| |7| |2|8|1|6|
|8| | | |6|1| | |9|
| | |1|5|8|9| | |2|
| |5| |8| |6| |2| |
| | | |2| | | |8| |
| |1| |9| |3| |7|4|
| | |5|6|2|4| | | |
|1| | |3| |8| | |5|
|4|3| |1| |5| |6|8|

There are 40 answers left to find.


 Iteration 2

|5|9| |7|3|2|8|1|6|
|8| | |4|6|1| |5|9|
| | |1|5|8|9| | |2|
| |5| |8| |6| |2| |
| | | |2| |7| |8| |
|2|1|8|9|5|3| |7|4|
| |8|5|6|2|4| | |7|
|1| | |3| |8| | |5|
|4|3| |1| |5| |6|8|

There are 31 answers left to find.


 Iteration 3

|5|9|4|7|3|2|8|1|6|
|8| | |4|6|1| |5|9|
| | |1|5|8|9| | |2|
| |5| |8| |6| |2| |
| | | |2| |7|5|8| |
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1| |7|
|1| | |3| |8| | |5|
|4|3| |1| |5| |6|8|

There are 26 answers left to find.


 Iteration 4

|5|9|4|7|3|2|8|1|6|
|8| | |4|6|1| |5|9|
| | |1|5|8|9| | |2|
| |5| |8|4|6| |2| |
| |4|9|2| |7|5|8| |
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1|3|7|
|1| | |3| |8| |9|5|
|4|3| |1| |5| |6|8|

There are 21 answers left to find.


 Iteration 5

|5|9|4|7|3|2|8|1|6|
|8| | |4|6|1| |5|9|
| | |1|5|8|9| |4|2|
| |5| |8|4|6|9|2|1|
|6|4|9|2|1|7|5|8| |
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1|3|7|
|1| |6|3|7|8|4|9|5|
|4|3| |1|9|5|2|6|8|

There are 11 answers left to find.


 Iteration 6

|5|9|4|7|3|2|8|1|6|
|8| |2|4|6|1| |5|9|
| |6|1|5|8|9| |4|2|
| |5| |8|4|6|9|2|1|
|6|4|9|2|1|7|5|8|3|
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1|3|7|
|1|2|6|3|7|8|4|9|5|
|4|3|7|1|9|5|2|6|8|

There are 6 answers left to find.


 Iteration 7

|5|9|4|7|3|2|8|1|6|
|8|7|2|4|6|1|3|5|9|
|3|6|1|5|8|9| |4|2|
|7|5|3|8|4|6|9|2|1|
|6|4|9|2|1|7|5|8|3|
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1|3|7|
|1|2|6|3|7|8|4|9|5|
|4|3|7|1|9|5|2|6|8|

There are 1 answers left to find.


 Iteration 8

|5|9|4|7|3|2|8|1|6|
|8|7|2|4|6|1|3|5|9|
|3|6|1|5|8|9|7|4|2|
|7|5|3|8|4|6|9|2|1|
|6|4|9|2|1|7|5|8|3|
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1|3|7|
|1|2|6|3|7|8|4|9|5|
|4|3|7|1|9|5|2|6|8|

There are 0 answers left to find.

Completed

|5|9|4|7|3|2|8|1|6|
|8|7|2|4|6|1|3|5|9|
|3|6|1|5|8|9|7|4|2|
|7|5|3|8|4|6|9|2|1|
|6|4|9|2|1|7|5|8|3|
|2|1|8|9|5|3|6|7|4|
|9|8|5|6|2|4|1|3|7|
|1|2|6|3|7|8|4|9|5|
|4|3|7|1|9|5|2|6|8|

SOLVED in 9 iterations in 0:00:00.003471

```

## Do you have any plans for the future?
Yes, lots thanks.

I hope to see this project through to completion but it's a hobby so I don't see it happening quickly. The long term aim is to get it to the point where someone can upload a photo of a sudoku puzzle and the app will return the solution. There's a good chance that someone (or many others) has already achieved this but I'm trying to avoid looking into other people's solutions as this is really a learning project for me.
