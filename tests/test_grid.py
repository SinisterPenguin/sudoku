import unittest

from sudoku.grid import Grid

TEST_GRID_FILE_PATH = r'C:\Users\benha\OneDrive\Documents\easy_sudoku.txt'


class Test3x3Grid(unittest.TestCase):
    def test_rows_012_from_box_0(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertListEqual(grid.rows_for_box(0), [0,1,2])

    def test_rows_345_from_box_5(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertListEqual(grid.rows_for_box(5), [3,4,5])

    def test_rows_678_from_box_7(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertListEqual(grid.rows_for_box(7), [6,7,8])

    def test_cols_345_from_box_1(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertListEqual(grid.cols_for_box(1), [3,4,5])

    def test_cols_012_from_box_3(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertListEqual(grid.cols_for_box(3), [0,1,2])

    def test_cols_678_from_box_8(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertListEqual(grid.cols_for_box(8), [6,7,8])

    def test_box_2_from_row_0_col_6(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertEqual(grid.box_from_row_col(0,6), 2)

    def test_box_3_from_row_5_col_1(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertEqual(grid.box_from_row_col(5,1), 3)

    def test_box_7_from_row_7_col_5(self):
        grid = Grid(TEST_GRID_FILE_PATH)
        self.assertEqual(grid.box_from_row_col(7,5), 7)