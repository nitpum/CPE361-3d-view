import turtle
import math
import numpy as np

from numpy.linalg import inv


def render_2d(points, edges, vertices, plane=(0, 1), offset=(0, 0), scale=1, filp=False, mirror=False):
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    t.hideturtle()
    wn.tracer(0, 0)
    t.penup()

    for edge in edges:
        t.penup()

        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]

        x_2d = p[plane[0]]
        y_2d = p[plane[1]]
        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        t.goto(x_2d, y_2d)

        p = vertices[to_edge]
        t.pendown()
        x_2d = p[plane[0]]
        y_2d = p[plane[1]]
        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        t.goto(x_2d, y_2d)

    wn.update()


def render_3d(points, edges, vertices, plane=(0, 1), offset=(0, 0), scale=1, filp=False, mirror=False):
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    t.hideturtle()
    wn.tracer(0, 0)
    t.penup()

    for edge in edges:
        t.penup()

        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]

        x = p[0]
        y = p[1]
        z = p[2]

        x_2d = (x / math.sin(math.radians(45))) + \
            (z / math.sin(math.radians(45)))
        y_2d = x + y - z

        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        t.goto(x_2d, y_2d)

        p = vertices[to_edge]
        t.pendown()
        x = p[0]
        y = p[1]
        z = p[2]

        x_2d = (x / math.sin(math.radians(45))) + \
            (z / math.sin(math.radians(45)))
        y_2d = x + y - z

        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        t.goto(x_2d, y_2d)

    wn.update()
