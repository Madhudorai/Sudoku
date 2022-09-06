#imports
import numpy as np
import random
import copy

difficulty = input("Enter difficulty (easy, medium,hard):")

#Functions
#print board fancy
def print_board(bo):
 for i in range(len(bo)):
  if i % 3 == 0 and i != 0:
   print("- - - - - - - - - - - - - ")

  for j in range(len(bo[0])):
   if j % 3 == 0 and j != 0:
    print(" | ", end="")

   if j == 8:
    print(bo[i][j])
   else:
    print(str(bo[i][j]) + " ", end="")

#find empty places in board (I.E 0)
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col
    return None

#valid board checking
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

#MAKE A COMPLETE FILLED BOARD
#fill empty board partially
def fill(bo):
  for i in range(1,25):
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    if bo[row][col] == 0:
      guess = random.randint(1,9)
      if valid(bo,guess,(row,col)):
        bo[row][col] = guess

#solving it to fully fill the board
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

matrix = np.zeros((9, 9), dtype=int)
fill(matrix)
mm = solve(matrix)

while mm == False: #ensuring correct output of board
    matrix = np.zeros((9, 9), dtype=int)
    fill(matrix)
    mm = solve(matrix)

solution = copy.deepcopy(matrix) #fully filled board is stored in solution

#REMOVE VALUES TO FORM PUZZLE
#solves for multiple sols. if 1 sol- counter = 1
def solveGrid(bo):
    global counter
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if bo[row][col] == 0:
            for value in range(1, 10):
                if valid(bo, value, [row, col]):
                    bo[row][col] = value
                    find = find_empty(bo)
                    if not find:
                        counter += 1
                        break
                    else:
                        if solveGrid(bo):
                            return True
            break
    bo[row][col] = 0


# REMOVE FROM FULLY FILLED SUDOKU BOARD
def removal(bo):
    global k
    global counter
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    while bo[x][y]!=0:
      backup = bo[x][y]
      bo[x][y] = 0
      solveGrid(bo)
      if counter == 1:
        k += 1
        counter = 0
        removal(bo)
      elif counter != 1 and difficulty == "easy" and k > 25:
        bo[x][y] = backup
        counter = 0
        return bo
      elif counter!=1 and difficulty == "medium" and k> 40:
        bo[x][y] = backup
        counter = 0
        return bo
      elif counter!=1 and difficulty == "hard" and k >50:
        bo[x][y] = backup
        counter = 0
        return bo
      else:
        bo[x][y] = backup
        counter = 0
        removal(bo)


k = 0
counter = 0
removal(matrix)
print("Q IS:")
puzzle = copy.deepcopy(matrix)
print_board(puzzle)

#Checking if puzzle is solvable and has unique solution
counter = 0
solveGrid(puzzle)
if counter==1:
    print("Haffun solving :)")
    print_board(solution)
