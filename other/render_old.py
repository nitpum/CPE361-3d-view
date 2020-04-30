import turtle
import math

GRID_SIZE = 1
MIN_POINT = (0, 0)
MAX_POINT = (300, 300)
BOARD_SIZE = (MAX_POINT[0] - MIN_POINT[0], MAX_POINT[1] - MIN_POINT[1])


def render(points, edges, vertices):
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    # t.hideturtle()
    # wn.tracer(0, 0)
    t.penup()

    # XZ pan
    for edge in edges:
        t.penup()

        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]

        x_2d = p[2] * 10
        y_2d = p[1] * 10
        t.goto(x_2d, y_2d)

        p = vertices[to_edge]
        t.pendown()
        x_2d = p[2] * 10
        y_2d = p[1] * 10
        t.goto(x_2d, y_2d)

    wn.update()
