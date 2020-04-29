import numpy as np


# def multVecMatrix(src dst):
#     S a, b, c, w

#     a = src[0] * x[0][0] + src[1] * x[1][0] + src[2] * x[2][0] + x[3][0]
#     b = src[0] * x[0][1] + src[1] * x[1][1] + src[2] * x[2][1] + x[3][1]
#     c = src[0] * x[0][2] + src[1] * x[1][2] + src[2] * x[2][2] + x[3][2]
#     w = src[0] * x[0][3] + src[1] * x[1][3] + src[2] * x[2][3] + x[3][3]

#     dst.x = a / w
#     dst.y = b / w
#     dst.z = c / w


def vectices_to_space(vertices, m):
    result = []
    for vertice in vertices:
        local_x = vertice[0]
        local_y = vertice[1]
        local_z = vertice[2]
        local_w = vertice[3]
        x = local_x * m[0][0] + local_y * m[1][0] + local_z * m[2][0] + m[3][0]
        y = local_y * m[0][1] + local_y * m[1][1] + local_z * m[2][1] + m[3][1]
        z = local_z * m[0][2] + local_y * m[1][2] + local_z * m[2][2] + m[3][2]
        # w = local_w * m[]
        result.append((x, y, z))
    return result


def world_space_to_camera_space(vertices):
    result = []
    for vertice in vertices:
        x = vertice[0] / -vertice[2]
        y = vertice[1] / -vertice[2]
        result.append((x, y))
    return result


def normalized_device(vertices, width, height):
    result = []
    for vertice in vertices:
        x = vertice[0]
        y = vertice[1]
        x = (x + width/2)/width
        y = (y + height/2)/height
        result.append((x, y))
    return result


def to_raster_space(vertices, width, height):
    result = []
    for vertice in vertices:
        x = vertice[0]
        y = vertice[1]
        x = x * width
        y = y * height
        result.append((x, y))
    return result
