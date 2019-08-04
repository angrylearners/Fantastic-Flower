import turtle


def main():
    window = turtle.Screen()
    babbage = turtle.Turtle()
    babbage.color("green", "black")
    babbage.speed("fast")
    babbage.left(90)
    babbage.fd(200)
    babbage.right(90)
    babbage.circle(20)
    for i in range(1, 24):
        petal(babbage)
    # name
    go(babbage, 200, -200)
    babbage.left(4)
    L(babbage)
    go(babbage, 250, -200)
    Z(babbage)
    go(babbage, 300, -200)
    H(babbage)
    babbage.hideturtle()
    window.exitonclick()


def petal(babbage):
    # if babbage.color() == ("red","black"):
    #     babbage.color("orange","black")
    # elif babbage.color() == ("orange", "black"):
    #     babbage.color("yellow", "black")
    # else:
    #     babbage.color("red","black")
    babbage.color("black", "black")
    babbage.left(15)
    babbage.forward(100)
    babbage.left(157)
    babbage.forward(100)


def L(babbage):
    babbage.right(90)
    babbage.forward(60)
    babbage.left(90)
    babbage.forward(40)


def Z(babbage):
    babbage.forward(40)
    babbage.right(120)
    babbage.goto(250, -260)
    babbage.left(120)
    babbage.forward(40)


def H(babbage):
    babbage.right(90)
    babbage.forward(60)
    babbage.back(30)
    babbage.left(90)
    babbage.forward(40)
    babbage.left(90)
    babbage.forward(30)
    babbage.back(60)


def go(babbage, x, y):
    babbage.penup()
    babbage.goto(x, y)
    babbage.pendown()


main()
