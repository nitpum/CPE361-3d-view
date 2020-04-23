# from render import *
import turtle


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


def render(points, edges, vertices, plane=(0, 1), offset=(0, 0), scale=1, filp=False, mirror=False):
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    t.hideturtle()
    wn.tracer(0, 0)
    t.penup()

    for edge in edges:
        t.penup()

        from_edge = edge[0] - 1
        to_edge = edge[1] - 1
        p = vertices[from_edge]

        x_2d = p[plane[0]]
        y_2d = p[plane[1]]
        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        t.goto(x_2d, y_2d)

        p = vertices[to_edge]
        t.pendown()
        x_2d = p[plane[0]]
        y_2d = p[plane[1]]
        if filp:
            y_2d *= -1
        if mirror:
            x_2d *= -1
        x_2d = x_2d * scale + offset[0]
        y_2d = y_2d * scale + offset[1]
        t.goto(x_2d, y_2d)

    wn.update()


GRID_SIZE = 1
MIN_POINT = (0, 0)
MAX_POINT = (300, 300)
BOARD_SIZE = (MAX_POINT[0] - MIN_POINT[0], MAX_POINT[1] - MIN_POINT[1])
SCALE = 50

vertices = []
edges = []
import_model("models/monkey.obj", edges, vertices)
render([], edges, vertices, (0, 2), (-150, 150), SCALE, True)
render([], edges, vertices, (0, 1), (-150, -150), SCALE)
render([], edges, vertices, (2, 1), (150, -150), SCALE, False, True)

# render([])
input("Press any key to exit... ")
