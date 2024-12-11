from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.__isrunning = False
        self.width = width
        self.height = height
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.isrunning = True
        while self.isrunning:
            self.redraw()

    def close(self):
        self.isrunning = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.__x1 = point_1.x
        self.__y1 = point_1.y
        self.__x2 = point_2.x
        self.__y2 = point_2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y2, fill = fill_color, width = 2)