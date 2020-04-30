import numpy as np
from numpy.linalg import inv
import math


def get_min_x(vertices):
    min_x = vertices[0][0]
    for vertice in vertices:
        if vertice[0] < min_x:
            min_x = vertice[0]
    return min_x


def get_min_y(vertices):
    min_y = vertices[0][1]
    for vertice in vertices:
        if vertice[1] < min_y:
            min_y = vertice[1]
    return min_y


def get_max_x(vertices):
    max_x = vertices[0][0]
    for vertice in vertices:
        if vertice[0] > max_x:
            max_x = vertice[0]
    return max_x


def get_max_y(vertices):
    max_y = vertices[0][1]
    for vertice in vertices:
        if vertice[1] > max_y:
            max_y = vertice[1]
    return max_y


def midpoint(x1, y1, x2, y2):
    return [(x1 + x2)/2, (y1 + y2)/2]


def vertices_midpoint(vertices):
    min_x = get_min_x(vertices)
    min_y = get_min_y(vertices)
    max_x = get_max_x(vertices)
    max_y = get_max_y(vertices)
    return midpoint(min_x, min_y, max_x, max_y)


def scale(points, to):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][0] * to[0], points[i][1] * to[1])
    return result


def rotate(points, degree):
    result = [] + points
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        sin = math.sin(math.radians(degree))
        cos = math.cos(math.radians(degree))
        result[i] = (x * cos - y * sin, x * sin + y * cos)
    return result


def translate(points, to):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][0] + to[0], points[i][1] + to[1])
    return result


def mirror(points):
    result = [] + points
    for i in range(len(points)):
        result[i] = (-points[i][0], points[i][1])
    return result


def flip(points):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][0], -points[i][1])
    return result


def flip45(points):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][1], points[i][0])
    return result


def swap_x(points):
    result = [] + points
    for i in range(len(points)):
        result[len(points) - 1 - i] = (points[i][0], points[i][1])
    return result


def swap_y(points):
    result = [] + points
    y_max = get_max_y(result)
    y_min = get_min_y(result)
    result = [] + translate(result, (0, -y_max))
    result = [] + flip(result)
    result = [] + translate(result, (0, y_min))
    return result


def matrix_inverse(matrix):
    return inv(np.array(matrix))


def edge_to_vertice(edge, vertices):
    from_edge = edge[0] - 1
    to_edge = edge[1] - 1
    p = vertices[from_edge]
    start = p

    p = vertices[to_edge]
    end = p
    return (start, end)
