import surface
import utils


def surfaces_z_sort(vertices, surfaces):
    sorted = [] + surfaces  # copy by value not ref

    for i in range(len(sorted)):  # selection sort
        run_index = i + 1
        swap = i
        while run_index < len(sorted):
            if (sorted[run_index].get_z(vertices) > sorted[i].get_z(vertices)):
                swap = run_index
            run_index = run_index + 1
        temp = sorted[i]
        sorted[i] = sorted[swap]
        sorted[swap] = temp
    return sorted


def surface_2d_hidden_line(edges, vertices, surface):
    remaing_edges = []
    hidden_edges = []
    for edge in edges:
        line = utils.edge_to_vertice(edge, vertices)
        result = surface.edge_intersect(vertices, line[0], line[1])
        if (result[0] == (-1, -1) and result[1] == (-1, -1)):
            remaing_edges.append(edge)
        else:
            hidden_edges.append(edge)
    return [remaing_edges, hidden_edges]


def get(vertices, surfaces):
    sorted = surfaces_z_sort(vertices, surfaces)
    print(sorted)
    remaing_edge = []
    hidden_edge = []
    for i in range(len(sorted)):
        surface_remaing_edge = sorted[i].edges
        surface_hidden_edge = []
        # Check other surface if other surface is higher in z axis

        for j in range(i):
            if sorted[j].get_z(vertices) > sorted[i].get_z(vertices):
                if i == 2:
                    print(sorted[j])
                result = surface_2d_hidden_line(
                    surface_remaing_edge, vertices, sorted[j])
                surface_remaing_edge = result[0]
                surface_hidden_edge = surface_hidden_edge + result[1]
                if i == 2:
                    print("Compare ", j)
                    print("Remaing ", result[0])

        # if i == 2:
        #     return [surface_remaing_edge, surface_hidden_edge]
        remaing_edge = remaing_edge + surface_remaing_edge
        hidden_edge = hidden_edge + surface_hidden_edge
    return [remaing_edge, hidden_edge]
