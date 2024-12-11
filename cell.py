from window import *



class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "#d9d9d9")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "#d9d9d9")
            
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "#d9d9d9")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "#d9d9d9")
    
    def draw_move(self, to_cell, undo = False):
        start_x = (self._x1 + self._x2) / 2
        start_y = (self._y1 + self._y2) / 2

        finish_x = (to_cell._x1 + to_cell._x2) / 2
        finish_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(start_x, start_y), Point(finish_x, finish_y))

        if not undo:
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(line, "gray")
             

#x - horizontal
#y - vertical