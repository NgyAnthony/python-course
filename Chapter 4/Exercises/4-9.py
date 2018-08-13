import turtle

hisa = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightgreen")
hisa.speed(0)

def draw_star(animal, length, angle):
    """
    Draw a 5 points star
    """
    for _ in range(5):
        animal.right(angle)
        animal.forward(length)


def move_away(animal, units, turn):
    """
    Move away from previous star
    """
    for _ in range(1):
        animal.penup()
        animal.forward(units)
        animal.right(turn)
        animal.pendown()


def summon_demon(animal, length, angle, units, turn):
    """
    Draw 5 stars
    """
    for _ in range(5):
        draw_star(animal, length, angle)
        move_away(animal, units, turn)


summon_demon(hisa, 100, 144, 350, 144)
window.mainloop()
