import turtle


def drawline(tur):
    for i in range(0,4):
        tur.forward(100)
        tur.right(90)

def draw_sq():
    brad = turtle.Turtle()
    drawline(brad)

def draw_circle():
    c = turtle.Turtle()
    c.circle(100)

def draw_square():
    
    window = turtle.Screen()
    window.bgcolor('red')

    draw_sq()
    draw_circle()

    window.exitonclick()

draw_square();
