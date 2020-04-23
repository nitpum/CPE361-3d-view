def import_model(file_name, edges, vertices):
    f = open(file_name)
    for line in f.readlines():
        l = line.rstrip('\n').split(' ')
        name = l[0]
        if name == 'v':
            vertices.append((float(l[1]), float(l[2]), float(l[3])))
        elif name == 'f':
            edges_list = l[1:]
            for i in range(len(edges_list)):
                if i == len(edges_list) - 1:
                    edges.append((int(edges_list[i]), int(edges_list[0])))
                else:
                    edges.append((int(edges_list[i]), int(edges_list[i + 1])))
    f.close()
