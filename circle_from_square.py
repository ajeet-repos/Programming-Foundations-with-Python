import turtle


def draw_sq(cur):
    for i in range(0,4):
        cur.forward(100)
        cur.right(90)

def draw_art():

    windows = turtle.Screen()
    windows.bgcolor('red')

    brad = turtle.Turtle()
    brad.color('yellow')

    for i in range(0,36):
        draw_sq(brad)
        brad.right(10)

    windows.exitonclick()

draw_art()
