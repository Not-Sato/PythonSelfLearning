import turtle
import easygui


def draw_square(size, color):
    turtle.penup()
    turtle.goto(-size / 2, -size / 2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def draw_triangle(size, color):
    turtle.penup()
    turtle.goto(-size / 2, -size / 2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()


def draw_circles(radius, color):
    fills = [color, "white"]
    for i in range(4):
        r = radius - i * radius / 4
        turtle.penup()
        turtle.goto(0, -r)
        turtle.pendown()
        turtle.fillcolor(fills[i % 2])
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()


def draw_star(size, color):
    turtle.penup()
    turtle.goto(-size / 2, 0)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def main():
    choice = easygui.buttonbox(
        "Choose a shape",
        "Geometric Pattern Studio",
        ["Square", "Equilateral Triangle", "Concentric Circles", "Custom Star"],
    )
    size = easygui.integerbox("Enter size (50 to 250)", "Size", lowerbound=50, upperbound=250)
    color = easygui.enterbox("Enter fill color (e.g. blue, red, teal)", "Color")

    if choice is None or size is None or color is None:
        return

    turtle.speed(5)

    if choice == "Square":
        draw_square(size, color)
    elif choice == "Equilateral Triangle":
        draw_triangle(size, color)
    elif choice == "Concentric Circles":
        draw_circles(size, color)
    else:
        draw_star(size, color)

    easygui.msgbox("Drawing completed!", "Done")
    turtle.bye()


main()