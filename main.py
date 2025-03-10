from graphics import Window
from cell import Cell

def main():
    window = Window(800, 600)

    # p1 = Point(50, 50)
    # p2 = Point(400, 200)
    # line = Line(p1, p2)
    #
    # window.draw_line(line, fill_color="red")

    cell = Cell(window)
    cell.draw(100, 200, 300, 400)
    cell.draw(200, 300, 400, 500)

    window.wait_for_close()

if __name__ == "__main__":
    main()

