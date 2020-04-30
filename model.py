from surface import Surface


def read_model(file_name, edges, vertices, surfaces):
    f = open(file_name)
    surface_id = 0
    for line in f.readlines():
        l = line.rstrip('\n').split(' ')
        flag = l[0]
        if flag == 'v':
            vertices.append((float(l[1]), float(l[2]), float(l[3])))
        elif flag == 'f':
            edges_list = l[1:]  # Edge list in string
            surface_edges = []
            for i in range(len(edges_list)):
                if i == len(edges_list) - 1:
                    edges.append((int(edges_list[i]), int(edges_list[0])))
                    surface_edges.append(
                        (int(edges_list[i]), int(edges_list[0])))
                else:
                    edges.append((int(edges_list[i]), int(edges_list[i + 1])))
                    surface_edges.append(
                        (int(edges_list[i]), int(edges_list[i + 1])))
            surface = Surface(surface_id, surface_edges)
            surfaces.append(surface)
            surface_id = surface_id + 1

    f.close()


def move_model_to_first_quadrant(edges, vertices):
    min_y = 0
    min_x = 0
    min_z = 0
    for vertice in vertices:
        x = vertice[0]
        y = vertice[1]
        z = vertice[2]
        if x <= min_x:
            min_x = x
        if y <= min_y:
            min_y = y
        if z <= min_z:
            min_z = z
    for i in range(len(vertices)):
        vertice = vertices[i]
        vertice = (vertice[0] - min_x, vertice[1] - min_y, vertice[2] - min_z)
        vertices[i] = vertice
