import argparse
from sudoku.grid import Grid

def display_grid():
    args = parse_args()
    grid = Grid(args.filepath)
    grid.print()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to file containing sudoku grid')
    return parser.parse_args()


if __name__=='__main__':
    display_grid()