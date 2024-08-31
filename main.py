#!/usr/bin/env python

"""
TODO: 
- Scan the board configuration from an image
- Output the board using tkinter
- Create a frontend to upload the image
"""
from pprint import PrettyPrinter
from enum import Enum, auto

pp = PrettyPrinter().pprint

class Color(Enum):
    PURP = auto()
    ORAN = auto()
    GREN = auto()
    GRAY = auto()
    TURQ = auto()
    RED = auto()
    BLUE = auto()
    PINK = auto()

board = [
    [Color.PURP, Color.PURP, Color.PURP, Color.PURP, Color.PURP, Color.PURP, Color.PURP, Color.PURP],
    [Color.PURP, Color.ORAN, Color.PURP, Color.PURP, Color.PURP, Color.BLUE, Color.BLUE, Color.PURP],
    [Color.ORAN, Color.ORAN, Color.GREN, Color.GREN, Color.GRAY, Color.GRAY, Color.BLUE, Color.BLUE],
    [Color.ORAN, Color.ORAN, Color.ORAN, Color.GREN, Color.GRAY, Color.BLUE, Color.BLUE, Color.BLUE],
    [Color.ORAN, Color.PINK, Color.ORAN, Color.TURQ, Color.RED, Color.BLUE, Color.BLUE, Color.BLUE],
    [Color.PINK, Color.PINK, Color.TURQ, Color.TURQ, Color.RED, Color.RED, Color.RED, Color.BLUE],
    [Color.PINK, Color.PINK, Color.PINK, Color.PINK, Color.PINK, Color.PINK, Color.RED, Color.BLUE],
    [Color.PINK, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]
]

solutions = []

def solve(board, row, running_sol: dict[int, tuple[int,int]], prev_col: int, verts: set[Color]):
    global solutions
    if row == len(board):
        solutions.append(running_sol.copy())
        return
    for column, color in enumerate(board[row]):
        # validate
        if color in running_sol:
            continue
        if column in verts:
            continue
        if column - 1 == prev_col or column + 1 == prev_col:
            continue
        running_sol[color] = (row, column)
        verts.add(column)
        solve(board, row+1, running_sol, column, verts)
        verts.remove(column)
        del running_sol[color]

solve(board, 0, {}, -2, set())
for solution in solutions:
    for color, coords in solution.items():
        solution[color] = (coords[0]+1, coords[1]+1)

pp(solutions)
