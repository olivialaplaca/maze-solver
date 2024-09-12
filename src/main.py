from window import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # line_1 = Line(Point(50, 50), Point(50, 200))
    # line_2 = Line(Point(600, 50), Point(600, 500))
    # line_1.draw(win.canvas, "black")
    # line_2.draw(win.canvas, "red")
    cell_1 = Cell(win)
    cell_1.has_bottom_wall = False
    cell_1.draw(Point(10, 10),Point(20, 20))
    cell_2 = Cell(win)
    cell_2.has_right_wall = False
    cell_2.draw(Point(50, 50), Point(100, 100))
    cell_3 = Cell(win)
    cell_3.has_top_wall = False
    cell_3.draw(Point(50, 150), Point(200, 200))

    cell_4 = Cell(win)
    cell_4.has_left_wall = False
    cell_4.draw(Point(300, 300), Point(450, 450))
    cell_4.draw_move(cell_3)
    m1 = Maze(300,300,4,4,20,20,win)
    m1._break_entrance_and_exit()
    win.wait_for_close()


main()
