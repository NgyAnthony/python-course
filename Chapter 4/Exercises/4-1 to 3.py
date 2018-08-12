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
Hisa = make_animal("Blue", 5, 1)  # Create turtle "Hisa".


def move_away(animal, size):
    """
    Move away from the square, made for make_five.
    To adapt for others.
    """
    print("Moving away")
    animal.forward(size)
    animal.penup()
    animal.forward(size)
    animal.pendown()  # Move away from previous square


def move_away_v2(animal):
    """
    Move away from the square, made for make_five.
    To adapt for others.
    """
    print("Moving away")
    animal.penup()
    animal.left(-90)
    animal.right(45)
    animal.forward(15)
    animal.right(225)
    animal.pendown()  # Move away from previous square


def draw_square(animal, size):
    """
    Make a square.
    """
    for _ in range(4):
        print("Tracing line number", _)
        animal.forward(size)
        animal.left(90)  # Make one square


def make_five(animal, size):
    """
    Make 5 squares separated for each other,
    choose who will draw it and the size of each side.
     """
    for _ in range(5):
        draw_square(animal, size)
        move_away(animal, size)


size_out = 20


def make_sqinsq(animal, size):
    """
    Make squares in squares based on animals and size of each squares
    """
    for _ in range(10):
        draw_square(animal, size)
        move_away_v2(animal)
        size += 20


def draw_poly(turtle, times, size):
    """
    Draw a polygon, choose your turtle, the number of sides and the size of your sides
    """
    for _ in range(times):
        turtle.forward(size)
        turtle.left(45)


wn.mainloop()  # Window stays open, keep it last or nothing will work.
