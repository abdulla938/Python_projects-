import turtle


canvas = turtle.Screen()

v_pen = turtle.Turtle()

v_pen.pensize(5)
v_pen.pencolor("Purple")
v_pen.hideturtle()

for _ in range(8):
    v_pen.forward(200)
    v_pen.right(45)

canvas.exitonclick()
