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
        seed=None
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
        if seed:
            random.seed(seed)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
        self._cells[i][j].draw(top_left, bottom_right)
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        self.win.root.after(50)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #adjacent cells -> i+1 (right) i-1 (left) j+1 (down) j-1 (up)
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            d = random.randint(0, len(to_visit)-1)
            direction = to_visit[d]
            # left
            if direction == (i-1, j):
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # right
            if direction == (i+1, j):
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # up
            if direction == (i, j-1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            # down
            if direction == (i, j+1):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
            
    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if i - 1 >= 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        if i + 1 < self.num_cols and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        if j - 1 >= 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        if j + 1 < self.num_rows and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False
            