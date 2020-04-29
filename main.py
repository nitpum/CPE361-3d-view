import turtle
from model import read_model, move_model_to_first_quadrant
from render import render, draw_line
from projection import vectices_to_space, world_space_to_camera_space, normalized_device, to_raster_space
import numpy as np
from numpy.linalg import inv

import math


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


# def draw_edge(edges, vertices):
#     wn = turtle.Screen()
#     t = turtle.Turtle()
#     t.speed(0)
#     t.pensize(1)
#     t.hideturtle()
#     wn.tracer(0, 0)
#     t.penup()

#     for edge in edges:
#           t.penup()

#           from_edge = edge[0] - 1
#           to_edge = edge[1] - 1
#           p = vertices[from_edge]

#           x_2d = p[plane[0]]
#           y_2d = p[plane[1]]
#           if filp:
#               y_2d *= -1
#           if mirror:
#               x_2d *= -1
#           x_2d = x_2d * scale + offset[0]
#           y_2d = y_2d * scale + offset[1]
#           t.goto(x_2d, y_2d)

#           p = vertices[to_edge]
#           t.pendown()
#           x_2d = p[plane[0]]
#           y_2d = p[plane[1]]
#           if filp:
#               y_2d *= -1
#           if mirror:
#               x_2d *= -1
#           x_2d = x_2d * scale + offset[0]
#           y_2d = y_2d * scale + offset[1]
#           t.goto(x_2d, y_2d)

#       wn.update()


def get_2d_view(edges, vertices, plane=(0, 1), offset=(0, 0), scale=1, filp=False, mirror=False):
    points = []
    for edge in edges:
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
        start = (x_2d, y_2d)

        p = vertices[to_edge]
        x_2d = p[plane[0]]
        y_2d = p[plane[1]]
        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        end = (x_2d, y_2d)

        # print(start, end, draw_line(start[0], start[1], end[0], end[1]))
        # print("Point ", start[0], start[1], end[0], end[1])
        line = draw_line(start[0], start[1], end[0], end[1])
        # print("Line ", line)
        points = [] + points + line
    return points


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


GRID_SIZE = 1
MIN_POINT = (0, 0)
MAX_POINT = (300, 300)
BOARD_SIZE = (MAX_POINT[0] - MIN_POINT[0], MAX_POINT[1] - MIN_POINT[1])
SCALE = 50

# vertices = [(2, 2, 0), (0, 0, 0)]
# vertices = [(2, 0, 0), (3, 4, 0)]
# edges = [(1, 2)]
vertices = []
edges = []
# read_model("models/cube.obj", edges, vertices)
read_model("models/triangle_long.obj", edges, vertices)
# read_model("models/cube.obj", edges, vertices)
# read_model("models/cube_long.obj", edges, vertices)
move_model_to_first_quadrant(edges, vertices)
render_3d([], edges, vertices, scale=20)
# camera([], edges, vertices, (0, 2), (-150, 150), SCALE, True)
# camera([], edges, vertices, (0, 1), (-150, -150), SCALE)
# camera([], edges, vertices, (2, 1), (150, -150), SCALE, False, True)

# print(vertices[1][1] - vertices[0][1] / vertices[1][0] - vertices[0][0])

# world_to_camera = [[0.718762, 0.615033, -0.324214, 0],
#                    [-0.393732, 0.744416, 0.539277, 0],
#                    [0.573024, -0.259959, 0.777216, 0],
#                    [0.526967, 1.254234, -2.53215, 1]]
# world_to_camera = [[0.871214, 0, -0.490904, 0],
#                    [-0.192902, 0.919559, -0.342346, 0],
#                    [0.451415, 0.392953, 0.801132, 0],
#                    [14.777467, 29.361945, 27.993464, 1]]

# world_to_camera = inv(np.array(world_to_camera))

# perspective = vectices_to_space(vertices, world_to_camera)

# for i in range(len(perspective)):
#     perspective[i] = (int(perspective[i][0]), int(
#         perspective[i][1]), int(perspective[i][2]))

# # print(perspective)
# screen = world_space_to_camera_space(perspective)
# # print(screen)
# norm = normalized_device(screen, 2, 2)
# raster = to_raster_space(norm, 512, 512)
# print(raster)
# camera([], edges, raster, plane=(0, 1),
#        scale=1, offset=(-150, -150))


# points_2d = get_2d_view(edges, vertices, plane=(0, 1), scale=1)
# render(10, 10, points_2d).save("result.png")

# print(vectices_to_space(vertices, [[0.718762, 0.615033, -0.324214, 0],
#                                    [-0.393732, 0.744416, 0.539277, 0],
#                                    [0.573024, -0.259959, 0.777216, 0],
#                                    [0.526967, 1.254234, -2.53215, 1]]))

input("Press any key to exit... ")
