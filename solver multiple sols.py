import random

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col
    return None


# valid
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


# SOLVER
def SolveGrid(bo):
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
                        print(bo) #if you want to print all the solutions
                        break
                    else:
                        if SolveGrid(bo):
                            return True
            break
    bo[row][col] = 0

#to implement print counter