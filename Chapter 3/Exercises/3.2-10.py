import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.speed(0)

def drunk():
    turns = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
    for turn in turns:
        tess.left(turn[0])
        tess.forward(turn[1])
        print("I am turning", turn[0])
        print("I am going taking", turn[1], "steps.")

def house():
    turns = [(90, 200), (-45, 200), (-90, 200), (-45, 200), (-125.5, 345), (-145, 280), (-145, 350), (145, 300)]
    for turn in turns:
        tess.left(turn[0])
        tess.forward(turn[1])
        print("I am turning", turn[0])
        print("I am going taking", turn[1], "steps.")


house()

window.mainloop()
