import numpy as np
import copy

class Sudoku:
    def __init__(self,sudoku):
        self.sudoku = sudoku

    # Returns list of the possible numbers that can fit
    def possibilities(self, i,j):
        row_possibilities = self.row_checker(i)
        col_possibilities = self.column_checker(j)
        square_possibilities = self.square_checker(i, j)

        inter = list(set(col_possibilities).intersection(row_possibilities))
        intersection = list(set(square_possibilities).intersection(inter))
        return intersection

    # Returns empty space position
    def empty_space(self):
        for i in range(len(self.sudoku)):
            for j in range(len(self.sudoku)):
                if self.sudoku[i][j]== 0:
                    return i, j
        return None, None

    # Checks row following sudoku rules
    def row_checker(self, row):
        nums = [1,2,3,4,5,6,7,8,9]
        for num in self.sudoku[row]:
            if num in nums:
                nums.remove(num)
        return nums

    # Checks column following sudoku rules
    def column_checker(self,col):
        nums = [1,2,3,4,5,6,7,8,9]
        for num in self.sudoku[:,col]:
            if num in nums:
                nums.remove(num)
        return nums

    # Checks 3x3 spaces following sudoku rules
    def square_checker(self,i,j):
        nums = [1,2,3,4,5,6,7,8,9]
        if i ==0 or i ==3 or i ==6:
            start = i
            end = i+2
        elif i==1 or i ==4 or i ==7:
            start = i-1
            end = i+1
        elif i==2 or i ==5 or i ==8:
            start = i-2
            end = i
        for row in range(start, end+1):
            if j ==0 or j == 3 or j ==6:
                start_j = j
                end_j = j+2
            elif j==1 or j==4 or j==7:
                start_j = j-1
                end_j = j+1
            elif j ==2 or j==5 or j==8:
                start_j = j-2
                end_j = j

            for col in range(start_j, end_j+1):
                if self.sudoku[row][col] in nums:
                    nums.remove(self.sudoku[row][col])

        return nums

def sudoku_solver(sudoku_object):
        i, j = sudoku_object.empty_space()
        if i == None:
            return True
        intersection =sudoku_object.possibilities(i,j)

        for num in intersection:
            sudoku_child = copy.deepcopy(sudoku_object)
            sudoku_child.sudoku[i][j] = num
            print(sudoku_child.sudoku)

            if sudoku_solver(sudoku_child) == True:
                return True
        return False


sudoku_table = np.array([
          [0,0,0,0,0,0,0,0,9],
          [0,4,6,3,0,1,5,8,7],
          [0,3,0,0,0,0,0,6,0],
          [0,7,0,6,0,4,0,2,0],
          [0,0,0,0,1,0,0,0,0],
          [0,1,0,7,0,8,0,3,0],
          [0,9,0,0,0,0,0,7,0],
          [5,6,2,1,0,9,8,4,0],
          [1,0,0,0,0,0,0,0,0]
])

sudoku = Sudoku(sudoku_table)
print(sudoku_solver(sudoku))

