import surface
import utils


def surfaces_z_sort(vertices, surfaces, debug=False):
    sorted = [] + surfaces  # copy by value not ref

    for i in range(len(sorted)):  # selection sort
        run_index = i + 1
        swap = i
        max_z = sorted[i].get_z(vertices)
        max_area = sorted[i].get_area(vertices)
        while run_index < len(sorted):
            comparator = sorted[run_index]
            if (comparator.get_z(vertices) > max_z) or (comparator.get_z(vertices) == max_z and comparator.get_area(vertices) > max_area):
                swap = run_index
                max_z = comparator.get_z(vertices)
                max_area = comparator.get_area(vertices)
            run_index = run_index + 1
        temp = sorted[i]
        sorted[i] = sorted[swap]
        sorted[swap] = temp
    return sorted


def edge_z(edge, vertices):
    line = utils.edge_to_vertice(edge, vertices)
    z = line[0][2]
    if line[1][2] < z:
        z = line[1][2]
    return z


def surface_2d_hidden_line(edges, vertices, surface, z, debug=False, i=0, j=0, target=None):
    remaing_edges = []
    hidden_edges = []
    for edge in edges:
        line = utils.edge_to_vertice(edge, vertices)
        intersected = surface.edge_intersect(
            vertices, line[0], line[1], debug=debug)
        if debug:
            print("intersect result: ", i, j, intersected)
        if intersected == False:
            remaing_edges.append(edge)
        else:
            hidden_edges.append(edge)
    return [remaing_edges, hidden_edges]


def get(vertices, surfaces, debug=False):
    sorted = surfaces_z_sort(vertices, surfaces, debug=debug)
    if debug:
        debug_index = 0
        for surface in sorted:
            print("S: ", debug_index, surface, surface.get_z(
                vertices), surface.get_area(vertices))
            debug_index = debug_index + 1
    remaing_edge = []
    hidden_edge = []
    for i in range(len(sorted)):
        surface_remaing_edge = sorted[i].edges
        surface_hidden_edge = []
        # Check other surface if other surface is higher in z axis

        if debug == True and i == 16:
            print("Start ", sorted[i], sorted[i].edges)

        for j in range(i):
            if sorted[j].get_z(vertices) > sorted[i].get_z(vertices) and sorted[j].get_area(vertices) > sorted[i].get_area(vertices):
                result = surface_2d_hidden_line(
                    surface_remaing_edge, vertices, sorted[j], sorted[j].get_z(vertices), debug=False, i=i, j=j, target=sorted[j])
                surface_remaing_edge = result[0]
                surface_hidden_edge = surface_hidden_edge + result[1]
                if debug == True and i == 16:
                    print("Compare ", j, sorted[j])
                    print("Remaing ", result[0])
                    print("Hidden ", result[1])

        # if i == 2:
        #     return [surface_remaing_edge, surface_hidden_edge]
        remaing_edge = remaing_edge + surface_remaing_edge
        hidden_edge = hidden_edge + surface_hidden_edge
    return [remaing_edge, hidden_edge]
