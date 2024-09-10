from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

    def redraw(self):
        self.root.update_idletasks() 
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close_window(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        self.canvas.create_line(line.p1.x, line.p1.y, line.p2.x, line.p2.y, fill=fill_color, width=2)
