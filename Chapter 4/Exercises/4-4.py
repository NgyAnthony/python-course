import turtle


def make_window(color, title):
    """
    Create a window along
    with a color and a title.
    """
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window


def make_animal(color, size, speed):
    """
    Create an animal,
    choose its color and its pensize.
    """
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    animal.speed(speed)
    return animal


wn = make_window("lightgreen", "I'm a turtle.")  # Create window
Hisa = make_animal("Blue", 5, 0)  # Create turtle "Hisa".


def cube(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


def cu_mv(animal, size, tilt):
    """
    Create a cube evenly separated in 4 cubes,
    tilts at the end.
    """
    for _ in range(2):
        cube(animal, size)
        animal.forward(size)
    animal.forward(-size*2)
    animal.left(-90)
    animal.forward(size)
    animal.left(90)
    for _ in range(2):
        cube(animal, size)
        animal.forward(size)
    animal.backward(size*2)
    animal.left(90)
    animal.forward(size)
    animal.right(90)
    animal.right(tilt)


def pretty(animal, size, tilt):
    """
    Calls the cu_mv function and makes it repeat
    a certain number of times
    """
    for _ in range(25):
        cu_mv(animal, size, tilt)


pretty(Hisa, 50, 15)
wn.mainloop()
