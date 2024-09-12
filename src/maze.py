from window import Point
from cell import Cell
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1= y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        self._cells = [[] for x in range(self.num_cols)]
        for i in range(len(self._cells)):
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        top_left = Point(self.x1 + self.cell_size_x * i, self.y1 + self.cell_size_y * j)
        bottom_right = Point(self.x1 + self.cell_size_x * (i + 1), self.y1 + self.cell_size_y * (j + 1))
        c = self._cells[i][j]
        c.draw(top_left, bottom_right)
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        self.win.root.after(50)

    def _break_entrance_and_exit(self):
        top_cell = self._cells[0][0]
        top_cell.has_top_wall = False
        self._draw_cell(0, 0)
        bottom_cell = self._cells[self.num_cols-1][self.num_rows-1]
        bottom_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)