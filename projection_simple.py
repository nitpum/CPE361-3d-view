import math


def parallel(edges, vertices, plane=(0, 1), view=(1, 1)):
    result = [] + vertices
    for edge in edges:
        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]

        x_2d = p[plane[0]] * view[0]
        y_2d = p[plane[1]] * view[1]
        result[from_edge] = (x_2d, y_2d)

        p = vertices[to_edge]
        x_2d = p[plane[0]] * view[0]
        y_2d = p[plane[1]] * view[1]
        result[to_edge] = (x_2d, y_2d)
    return result


def perspective(edges, vertices, plane=(0, 1)):
    result = [] + vertices
    for edge in edges:
        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]
        x = p[0]
        y = p[1]
        z = p[2]

        x_2d = (x / math.sin(math.radians(45))) + \
            (z / math.sin(math.radians(45)))
        y_2d = x + y - z
        result[from_edge] = (x_2d, y_2d)

        p = vertices[to_edge]
        x = p[0]
        y = p[1]
        z = p[2]
        x_2d = (x / math.sin(math.radians(45))) + \
            (z / math.sin(math.radians(45)))
        y_2d = x + y - z
        result[to_edge] = (x_2d, y_2d)
    return result
