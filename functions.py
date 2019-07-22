from collections import Counter
import json

# Create a new puzzle with no values
def generate_new_puzzle():
  puzzle = []
  row = 0
  while row <= 8:
    col = 0
    puzzle.append([])
    while col <= 8:
      puzzle[row].append("")
      col += 1
    row += 1
  return puzzle

# Adds a list of values to the puzzle
# Expects values as {(x, y) : int, (x, y) : int, ...}
def add_values_to_puzzle(values, puzzle):
  for coordinates, value in values.items():
    x, y = coordinates
    puzzle[x][y] = value
  return puzzle

# Return a list of the locations of empty cells
# Return format [(x, y), (x, y), ...]
def get_empty_cell_locations(puzzle):
  empty_cells = []
  row_no = 0
  for row in puzzle:
    col_no = 0
    for value in row:
      if value is "":
        empty_cells.append((row_no, col_no))
      col_no += 1
    row_no += 1
  return empty_cells

# Prints the puzzle to the command line
def print_the_puzzle(puzzle):
  print("")
  for row in puzzle:
    contents = "|"
    for value in row:
      if value is "":
        contents += value + " |"
      else:
        contents += str(value) + "|"
    print(contents)

# Return a dictionary of valid answers for each empty cell
# Return format {(x, y) : [int, int, ...], (x, y) : [int, int ...], ...}
def get_all_valid_answers(puzzle):
  empty_cells = get_empty_cell_locations(puzzle)
  all_valid_answers = {}
  cell_answers = []
  invalid_answers = []
  answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  for cell in empty_cells:
    invalid_answers = get_invalid_answers(cell, puzzle)
    cell_answers = list(set(answers) - set(invalid_answers))
    cell_answers.sort()
    all_valid_answers.update({cell : cell_answers})

  return all_valid_answers

# Return a list of all invalid answers for a given cell coordinate (x, y)
# Return format [int, int, int, ...]
def get_invalid_answers(coordinate, puzzle):
  x, y = coordinate
  row_values = puzzle[x]
  col_values = []
  box_values = []
  box_coordinates = get_box_coordinates(coordinate)
  used_values = []

  for row in puzzle:
    col_values.append(row[y])

  for cell in box_coordinates:
    cell_x, cell_y = cell
    box_values.append(puzzle[cell_x][cell_y])

  used_values = row_values + col_values + box_values
  used_values = list(dict.fromkeys(used_values))
  used_values.remove("")
  used_values.sort()
  return used_values

# Return a list of the coordinates of all the cells in the box
# the specified cell is in [(x, y), (x, y), ...]
def get_box_coordinates(coordinate):
  x, y = coordinate
  if x <= 2:
    # first row
    if y <= 2:
      box_coordinates = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    elif y <= 5:
      box_coordinates = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
    elif y <= 8:
      box_coordinates = [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]
  elif x <= 5:
    # second row
    if y <= 2:
      box_coordinates = [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)]
    elif y <= 5:
      box_coordinates = [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
    elif y <= 8:
      box_coordinates = [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]
  elif x <= 8:
    # third row
    if y <= 2:
      box_coordinates = [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)]
    elif y <= 5:
      box_coordinates = [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]
    elif y <= 8:
      box_coordinates = [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]
  return box_coordinates

# Return a dictionary of any cell that only has one valid answer with its coordinates
# Return format {(x, y) : int, (x, y) : int, ...}
def find_cells_with_one_answer(answers):
  output = {}
  for coordinate, values in answers.items():
    if len(values) == 1:
      output.update({coordinate : int(values[0])})
  return output

# Check all valid answers in a box for any unique values
# Return format {(x, y) : int, (x, y) : int, ...}
def check_boxes_for_unique_values(answers):
  row = 0
  output = {}
  while row <= 8:
    this_box = {}
    box_values = []
    col = 0
    while col <= 8:
      box_coordinates = get_box_coordinates((row, col))
      for coordinate in box_coordinates:
        if coordinate in answers:
          this_box.update({coordinate : answers[coordinate]})
          for answer in answers[coordinate]:
            box_values.append(answer)
      for value, count in Counter(box_values).most_common():
        if count == 1:
          unique_answer = ""
          unique_answer = value
          for coordinate, values in this_box.items():
            for value in values:
              if value == unique_answer:
                output.update({coordinate : value})
      col += 3
    row += 3
  return output

# Check all values in rows or columns for any unique values
# Return format {(x, y) : int, (x, y) : int, ...}
def check_rows_and_cols_for_unique_values(answers):
  output = {}

  # transform the answer list into a grid
  grid = generate_new_puzzle()
  for coordinate, values in answers.items():
    x, y = coordinate
    grid[x][y] = values

  # check for unique values in rows
  row_no = 0
  for row in grid:
    this_row = []
    for cell in row:
      for value in cell:
        this_row.append(value)
    # print(this_row)
    for value, count in Counter(this_row).most_common():
      if count == 1:
        unique_answer = ""
        unique_answer = value
        for coordinate, values in answers.items():
          x, y = coordinate
          if x == row_no:
            for value in values:
              if value == unique_answer:
                output.update({coordinate : value})
    row_no += 1

  # check for unique values in columns
  col_no = 0
  while col_no <= 8:
    this_col = []
    row_no = 0
    while row_no <= 8:
      if (row_no, col_no) in answers:
        for value in answers[(row_no, col_no)]:
          this_col.append(value)
      row_no += 1
    for value, count in Counter(this_col).most_common():
      if count == 1:
        unique_answer = ""
        unique_answer = value
        for coordinate, values in answers.items():
          x, y = coordinate
          if y == col_no:
            for value in values:
              if value == unique_answer:
                output.update({coordinate : value})
    col_no += 1
  return output

# dump the puzzle into a JSON file with the name filename.json
def output_puzzle_as_json(puzzle, filename):
	the_filename = filename + ".json"
	with open(the_filename, 'w') as json_file:
	  json.dump(puzzle, json_file)
