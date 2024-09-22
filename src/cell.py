from window import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, top_left_corner, bottom_right_corner):
        if not self._win:
            return
        self._x1 = top_left_corner.x
        self._y1 = top_left_corner.y
        self._x2 = bottom_right_corner.x
        self._y2 = bottom_right_corner.y

        top_wall = Line(top_left_corner, Point(bottom_right_corner.x, top_left_corner.y))
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")
        left_wall = Line(top_left_corner, Point(top_left_corner.x, bottom_right_corner.y))
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")
        bottom_wall = Line(Point(top_left_corner.x, bottom_right_corner.y), bottom_right_corner)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")
        right_wall = Line(bottom_right_corner, Point(bottom_right_corner.x, top_left_corner.y))
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")

    def draw_move(self, to_cell, undo=False):
        center_of_self = Point((self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2)
        center_to_cell = Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y2 + to_cell._y1) / 2)
        if not undo:
            line_color = "red"
        else:
            line_color = "gray"
        self._win.draw_line(Line(center_of_self, center_to_cell), line_color)
