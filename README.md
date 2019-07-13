# Sudoku Solver
I had been wondering for a while if I could write a script that would solve sudoku puzzles and I also wanted to learn Python. This is an *attempt* at both.

## So what does it do right now?
Currently this project runs on the command line `python3 sudoku.py` and it will only solve fairly simple 9x9 Sudoku puzzles.

## How does it work?
- Makes a list of all the cells that are empty
- Calculates all valid answers for every empty cell
- Looks for cells that only have one valid answer
- Looks for answers that only have one valid position within a 3x3 box
- Inserts the valid answers
- Loops back through the first five steps until all answers have been found
- ... or fails if the number of answers left does not decrease after an iteration

## How is the puzzle stored?
There is a single dictionary that stores every location (cell) and its value. The locations are two digits which act as co-ordinates - the first digit is the row number and the second is the column number. Like this:

```
   1  2  3  4  5  6  7  8  9
1 |11|12|13|14|15|16|17|18|19|
2 |21|22|23|24|25|26|27|28|29|
3 |31|32|33|34|35|36|37|38|39|
4 |41|42|43|44|45|46|47|48|49|
5 |51|52|53|54|55|56|57|58|59|
6 |61|62|63|64|65|66|67|68|69|
7 |71|72|73|74|75|76|77|78|79|
8 |81|82|83|84|85|86|87|88|89|
9 |91|92|93|94|95|96|97|98|99|
```


## Example output
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

## Do you have any plans for the future?
Yes, lots thanks.

I hope to see this project through to completion but it's a hobby so I don't see it happening quickly. The long term aim is to get it to the point where someone can upload a photo of a sudoku puzzle and the app will return the solution. There's a good chance that someone (or many others) has already achieved this but I'm trying to avoid looking into other people's solutions as this is really a learning project for me.
