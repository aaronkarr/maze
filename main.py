from graphics import Point, Window, Line


def main():
    window = Window(800, 600)

    p1 = Point(50, 50)
    p2 = Point(400, 200)
    line = Line(p1, p2)

    window.draw_line(line, fill_color="red")

    window.wait_for_close()

if __name__ == "__main__":
    main()

