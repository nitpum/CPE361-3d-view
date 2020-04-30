import turtle
import math
import numpy as np
from numpy.linalg import inv
import utils


def render(edges, vertices, scale=(1, 1), position=(0, 0), offset=(0, 0), color="black"):
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    t.hideturtle()
    wn.tracer(0, 0)
    t.pencolor(color)
    t.penup()

    # copy by value
    local_vertices = [] + vertices

    # find center of object
    midpoint = utils.vertices_midpoint(local_vertices)

    # adjust scale and position
    # move center of object to origin point for ease implulation
    local_vertices = utils.translate(
        local_vertices, [-midpoint[0], -midpoint[1]])

    local_vertices = utils.scale(local_vertices, scale)

    min_x = utils.get_min_x(local_vertices)
    min_y = utils.get_max_y(local_vertices)

    local_vertices = utils.translate(
        local_vertices, (-min_x + offset[0] + position[0], min_y + offset[1] + position[1]))

    # drawing
    for edge in edges:
        t.penup()

        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = local_vertices[from_edge]

        x_2d = p[0]
        y_2d = p[1]
        t.goto(x_2d, y_2d)

        p = local_vertices[to_edge]
        t.pendown()
        x_2d = p[0]
        y_2d = p[1]
        t.goto(x_2d, y_2d)

    wn.update()
