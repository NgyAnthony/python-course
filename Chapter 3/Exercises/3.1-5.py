import turtle

tess = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightgreen")
tess.shape("turtle")
tess.speed(0)

def polygon_triangle():
    for i in range(2):
        tess.forward(100)
        tess.left(120)
    tess.forward(100)
    tess.right(60)
    tess.penup()
    tess.forward(100)

def polygon_square():
    for i in range(4):
        tess.forward(100)
        tess.left(90)

def polygon_hexagon():
    tess.penup()
    tess.forward(100)
    tess.pendown()
    for i in range(6):
        tess.left(60)
        tess.forward(100)
    tess.penup()
    tess.left(120)
    tess.forward(100)
    tess.right(120)

def polygon_octogon():
    tess.penup()
    tess.forward(100)
    tess.pendown()
    for i in range(8):
        tess.left(45)
        tess.forward(100)
    tess.penup()
    tess.forward(100)

polygon_octogon()
window.mainloop()
