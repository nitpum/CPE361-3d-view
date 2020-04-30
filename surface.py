import line_clipping
import utils


class Surface:
    id = -1
    edges = []

    def __init__(self, id,  edges_list):
        self.edges = edges_list
        self.id = id

    def get_z(self, vertices):
        z = 0
        first = False
        for edge in self.edges:
            from_edge = edge[0] - 1
            to_edge = edge[1] - 1
            p = vertices[from_edge]
            if first == False:
                first = True
                z = p[2]
            if p[2] > z:
                z = p[2]
            p = vertices[to_edge]
            if p[2] > z:
                z = p[2]
        return z

    def __repr__(self):
        return "Surface " + str(self.id)

    def __str__(self):
        return "Surface " + str(self.id)

    def edge_intersect(self, vertices, start_line, end_line):
        local_vertice = []
        for edge in self.edges:
            from_edge = edge[0] - 1
            to_edge = edge[1] - 1
            p = vertices[from_edge]

            x_2d = p[0]
            y_2d = p[1]
            start = (x_2d, y_2d)
            if start not in local_vertice:
                local_vertice.append(start)

            p = vertices[to_edge]
            x_2d = p[0]
            y_2d = p[1]
            end = (x_2d, y_2d)
            if end not in local_vertice:
                local_vertice.append(end)
        return line_clipping.cyrus_beck(local_vertice, (start_line, end_line))
