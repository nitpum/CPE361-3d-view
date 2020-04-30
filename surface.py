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

    def get_area(self, vertices):
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        first = True
        for edge in self.edges:
            line = utils.edge_to_vertice(edge, vertices)
            if line[0][0] < min_x or first:
                min_x = line[0][0]
            if line[0][0] > max_x or first:
                max_x = line[0][0]
            if line[0][1] < min_y or first:
                min_y = line[0][1]
            if line[0][1] > max_y or first:
                max_y = line[0][1]

            if first:
                first = False

            if line[1][0] < min_x:
                min_x = line[1][0]
            if line[1][0] > max_x:
                max_x = line[1][0]
            if line[1][1] < min_y:
                min_y = line[1][1]
            if line[1][1] > max_y:
                max_y = line[1][1]
        width = max_x - min_x
        height = max_y - min_y
        return width * height

    def __repr__(self):
        return "Surface " + str(self.id)

    def __str__(self):
        return "Surface " + str(self.id)

    def edge_intersect(self, vertices, start_line, end_line, debug=False):
        local_vertice = []

        # for edge in self.edges:
        #     from_edge = edge[0] - 1
        #     to_edge = edge[1] - 1
        #     p = vertices[from_edge]

        #     x_2d = p[0]
        #     y_2d = p[1]
        #     start = (x_2d, y_2d)
        #     if start not in local_vertice:
        #         local_vertice.append(start)

        #     p = vertices[to_edge]
        #     x_2d = p[0]
        #     y_2d = p[1]
        #     end = (x_2d, y_2d)
        #     if end not in local_vertice:
        #         local_vertice.append(end)

        # intersected = line_clipping.cyrus_beck(
        #     local_vertice, (start_line, end_line))

        result = False
        # if intersected != [(-1, -1), (-1, -1)]:
        #     result = True

        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        first = True
        for edge in self.edges:
            line = utils.edge_to_vertice(edge, vertices)
            if line[0][0] < min_x or first:
                min_x = line[0][0]
            if line[0][0] > max_x or first:
                max_x = line[0][0]
            if line[0][1] < min_y or first:
                min_y = line[0][1]
            if line[0][1] > max_y or first:
                max_y = line[0][1]

            if first:
                first = False

            if line[1][0] < min_x:
                min_x = line[1][0]
            if line[1][0] > max_x:
                max_x = line[1][0]
            if line[1][1] < min_y:
                min_y = line[1][1]
            if line[1][1] > max_y:
                max_y = line[1][1]
        if (start_line[0] < max_x and start_line[0] > min_x and start_line[1] > min_y and start_line[1] < max_y) \
                or (end_line[0] < max_x and end_line[0] > min_x and end_line[1] > min_y and end_line[1] < max_y):
            result = True
        if debug:
            print("R: ", result, start_line, end_line,
                  (min_x, min_y), (max_x, max_y))
        return result
