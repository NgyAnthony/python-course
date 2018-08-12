import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.shape("turtle")

def polygon_twelve():
    for i in range(12):
        tess.penup()
        tess.forward(75)
        tess.pendown()
        tess.forward(10)
        tess.penup()
        tess.forward(15)
        tess.stamp()
        tess.forward(-100)
        tess.left(30)

polygon_twelve()
window.mainloop()
