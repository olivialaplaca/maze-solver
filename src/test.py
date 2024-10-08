import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_2cells(self):
        num_cols = 2
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_100cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_entrance_and_exit(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[2][2].has_bottom_wall,
            False
        )

    def test_maze_borders(self):
        num_cols = 4
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        top_edge = []
        for i in range(1, m1.num_cols):
            top_edge.append(m1._cells[i][0])
        for cell in top_edge:
            self.assertEqual(
                cell.has_top_wall,
                True
            )
        bottom_edge = []
        for i in range(m1.num_cols-1):
            bottom_edge.append(m1._cells[i][-1])
        for cell in bottom_edge:
            self.assertEqual(
                cell.has_bottom_wall,
                True
            )
        for cell in m1._cells[0]:
            self.assertEqual(
                cell.has_left_wall,
                True
            )
        for cell in m1._cells[-1]:
            self.assertEqual(
                cell.has_right_wall,
                True
            )

    def test_reset_visit(self):
        num_cols = 4
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        for i in range(m1.num_cols):
            for j in range(m1.num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()