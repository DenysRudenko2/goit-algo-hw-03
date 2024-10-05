import turtle

SIZE = 300


def koch_snowflake(t: turtle, order: int, size: float = SIZE):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)


def draw_koch_snowflake(order):
    t = turtle.Turtle()
    t.penup()
    t.setposition(-SIZE/2, SIZE/2)
    t.pendown()
    t.speed(0)

    for _ in range(3):
        koch_snowflake(t, order)
        t.right(120)

    t.hideturtle()
    turtle.Screen().exitonclick()


draw_koch_snowflake(3)
