from window import *
from cell import *
from maze import *

win = Window(1600, 1200)
maze = Maze(10, 10, 15, 15, 20, 20, win)
maze.solve(0,0)
win.wait_for_close()