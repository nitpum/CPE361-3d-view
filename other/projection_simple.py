import math


def redline(edges, vertices,  plane=(0, 1), view=(1, 1)):
    result_edges = []
    result_vertice = []
    vertice_index = 0
    for edge in edges:
        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]

        x_2d = p[plane[0]] * view[0]
        y_2d = p[plane[1]] * view[1]
        start = (x_2d, y_2d)

        p = vertices[to_edge]
        x_2d = p[plane[0]] * view[0]
        y_2d = p[plane[1]] * view[1]
        end = (x_2d, y_2d)

        if (start[0] == end[0]):
            result_vertice.append((start[0], -500))
            result_vertice.append((start[0], 500))
            result_edges.append((vertice_index, vertice_index + 1))
            vertice_index = vertice_index + 1
        elif (start[1] == end[1]):
            result_vertice.append((-500, start[1]))
            result_vertice.append((500, start[1]))
            result_edges.append((vertice_index, vertice_index + 1))
            vertice_index = vertice_index + 1
    return [result_edges, result_vertice]


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
