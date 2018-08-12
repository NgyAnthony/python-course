import turtle
tess = turtle.Turtle()
window = turtle.Screen()
tess.shape("turtle")

def star_shape():
    for i in range(5):
        tess.left(36)
        tess.forward(100)
        tess.right(108)
        tess.forward(100)

def main_star():
    for i in range(5):
        tess.right(144)
        tess.forward(150)

main_star()
window.mainloop()
