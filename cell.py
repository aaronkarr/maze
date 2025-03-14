from graphics import Line, Point


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__window = window

    def draw(self, x1, y1, x2, y2):
        if self.__window is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        if self.has_left_wall:
            self.__window.draw_line(left_wall)
        else:
            self.__window.draw_line(left_wall, fill_color="white")
        if self.has_right_wall:
            self.__window.draw_line(right_wall)
        else:
            self.__window.draw_line(right_wall, fill_color="white")
        if self.has_top_wall:
            self.__window.draw_line(top_wall)
        else:
            self.__window.draw_line(top_wall, fill_color="white")
        if self.has_bottom_wall:
            self.__window.draw_line(bottom_wall)
        else:
            self.__window.draw_line(bottom_wall, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        move_x = (self.__x1 + self.__x2) // 2
        move_y = (self.__y1 + self.__y2) // 2
        move_to_x = (to_cell.__x1 + to_cell.__x2) / 2
        move_to_y = (to_cell.__y1 + to_cell.__y2) / 2
        move_line = Line(Point(move_x, move_y), Point(move_to_x, move_to_y))

        fill_color = "red"
        if undo:
            fill_color = "gray"
        self.__window.draw_line(move_line, fill_color=fill_color)
