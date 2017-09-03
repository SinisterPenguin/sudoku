import math
import copy
from collections import namedtuple

class UnsquareGridError(Exception):
    pass

Assignment = namedtuple('Assignment', 'row col value')

class Grid():
    def __init__(self, path):
        self.__cells = Grid.__from_file(path)
        self.__original_cells = copy.deepcopy(self.__cells)
        self.size = int(len(self.__cells))
        self.root = int(math.sqrt(self.size))
        self.alphabet = sorted({a for a in Grid.__yield_all_cells(self.__cells) if a})
        self.__moves_made = []

    def reset(self):
        self.__cells = copy.deepcopy(self.__original_cells)
        self.__moves_made = []

    @staticmethod
    def __yield_all_cells(cells):
        for row in cells:
            for cell in row:
                yield cell

    @staticmethod
    def __from_file(path):
        with open(path) as file:
            length = 0
            rownum = 1
            cells = []
            for line in file:
                row = [x if x.isalnum() else None for x in line.strip()]

                if length == 0:
                    length = len(row)
                elif len(row) != length:
                    raise UnsquareGridError("Inconsistent row lengths")

                if rownum > length:
                    raise UnsquareGridError("Too many rows")

                rownum += 1
                cells.append(row)

        if rownum < length:
            raise UnsquareGridError("Too few rows")

        if not math.sqrt(length) == int(math.sqrt(length)):
            raise UnsquareGridError("Grid size is not a square number")

        return cells

    def assign(self, row, col, value):
        value = str(value)
        box = self.box_from_row_col(row, col)

        if self.__cells[row][col] is not None:
            raise ValueError("Cell already has a value assigned")
        elif value in self.__row(row):
            raise ValueError("Value {} already in row {}: {}".format(value, row, self.printable_row(row)))
        elif value in self.__col(col):
            raise ValueError("Value {} already in col {}: {}".format(value, col, self.printable_col(col)))
        elif value in self.__box(box):
            raise ValueError("Value {} already in box {}: {}".format(value, box, self.printable_box(box)))
        else:
            print("Assigning {} to row {} column {}".format(value, row, col))
            self.__cells[row][col] = value
            self.__moves_made.append(Assignment(row, col, value))

    def list_moves(self):
        for move in self.__moves_made:
            print(move)

    def undo_assign(self):
        last_move = self.__moves_made.pop()
        self.__cells[last_move.row][last_move.col] = None

    def print(self):
        print("Displaying {0:0d}x{0:0d} grid:".format(self.size))
        for row_num in range(self.size):
            print(self.printable_row(row_num))

    def __row(self, row_num):
        return self.__cells[row_num]

    def __col(self, col_num):
        return [x[col_num] for x in self.__cells]

    def __box(self, box_num):
        return [self.__cells[x][y] for x in self.rows_for_box(box_num) for y in self.cols_for_box(box_num)]

    def rows_for_box(self, box_num):
        for first_row in range(0, self.size, self.root):
            if first_row + self.root > box_num:
                return [row for row in range(first_row, first_row + self.root)]

    def cols_for_box(self, box_num):
        for col_band in range(0, self.root):
            if box_num % self.root == col_band:
                first_col = self.root * col_band
                return [col for col in range(first_col, first_col + self.root)]

    def box_from_row_col(self, row, col):
        return 3*(row//self.root) + col//self.root

    def printable_row(self, row_num):
        return ''.join(x if x else '.' for x in self.__row(row_num))

    def printable_col(self, col_num):
        return ''.join(x if x else '.' for x in self.__col(col_num))

    def printable_box(self, box_num):
        return ''.join(x if x else '.' for x in self.__box(box_num))

if __name__=='__main__':
    grid = Grid('C:\\Users\\benha\\OneDrive\\Documents\\easy_sudoku.txt')
    grid.print()