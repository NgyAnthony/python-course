import turtle

tess = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightgreen")
tess.shape("turtle")
tess.speed(0)

drunk_walk = [160, -43, 270, -97, -43, 200, -940, 17, -86]

def drunk_path():
    for walk in drunk_walk:
        tess.left(walk)
        tess.forward(100)

    for heading in drunk_walk:
        current_heading = 0
        current_heading += heading % 360
        print(current_heading)

drunk_path()

window.mainloop()

#For a regular polygon with 18 sides I'd choose a 20° angle.