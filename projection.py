import numpy as np
import math
import utils


def vectices_to_space(vertices, m):
    result = []
    for vertice in vertices:
        local_x = vertice[0]
        local_y = vertice[1]
        local_z = vertice[2]
        x = local_x * m[0][0] + local_y * m[1][0] + local_z * m[2][0] + m[3][0]
        y = local_y * m[0][1] + local_y * m[1][1] + local_z * m[2][1] + m[3][1]
        z = local_z * m[0][2] + local_y * m[1][2] + local_z * m[2][2] + m[3][2]
        # w = local_w * m[]
        result.append((x, y, z))
    return result


def normalized_device(vertices):
    result = []
    min_x = utils.get_min_x(vertices)
    min_y = utils.get_min_y(vertices)
    max_x = utils.get_max_x(vertices)
    max_y = utils.get_max_y(vertices)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(max_y, min_y)
    for vertice in vertices:

        x = vertice[0]
        y = vertice[1]
        # x = (x - min_x)/width
        # y = (y - min_y)/height
        result.append((x, y))
    return result


def to_raster_space(vertices, width, height):
    result = []
    for vertice in vertices:
        x = vertice[0]
        y = vertice[1]
        x = x * width
        y = y * height
        result.append((math.floor(x), math.floor(y)))
    return result
