import turtle

hisa = turtle.Turtle()
window = turtle.Screen()
window.title("Spiral")
window.bgcolor("lightgreen")
hisa.speed(0)


def spiral(animal, dist, angle, incr, segs):
    for _ in range(segs):
        animal.forward(dist)
        animal.right(angle)
        dist += incr


spiral(hisa, 2, 89.5, 2, 184)

window.mainloop()

# code from https://commons.wikimedia.org/wiki/File:Turtle-Graphics_Polyspiral.svg
