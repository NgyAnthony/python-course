import turtle
hisa = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightblue")


def draw_poly(turtle, times, size, angle):
    """
    Draw a polygon, choose your turtle,
    the number of sides, the size of your sides and
    the angle you choose.
    """
    for _ in range(times):
        turtle.forward(size)
        turtle.left(angle)


def draw_equitriangle(turtle, size, angle):
    """
    Draws an equilateral triangle based on function polygon
    """
    draw_poly(turtle, 3, size, angle)


draw_equitriangle(hisa, 40, 120)

window.mainloop()