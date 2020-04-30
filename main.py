
import turtle
from model import read_model, move_model_to_first_quadrant
from render_turtle import render
import render as rd
import projection_simple
import projection
import utils
import line_intersect
import hidden_line

# Configuration
WINDOW_WIDTH = 1027
WINDOW_HEIGHT = 600
MODEL_FILE = "models/stair.obj"
GRID_SIZE = 1
MIN_POINT = (0, 0)
MAX_POINT = (300, 300)
BOARD_SIZE = (MAX_POINT[0] - MIN_POINT[0], MAX_POINT[1] - MIN_POINT[1])
SCALE = (25, 25)
SCALE_3d = (10, 10)

wn = turtle.Screen()
wn.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

vertices = []
edges = []
surfaces = []


# Model
read_model(MODEL_FILE, edges, vertices, surfaces)

# Projection
top_view = projection_simple.parallel(edges, vertices, plane=(0, 2))
bottom_view = projection_simple.parallel(
    edges, vertices, plane=(0, 2), view=(1, -1))
front_view = projection_simple.parallel(edges, vertices, plane=(0, 1))
back_view = projection_simple.parallel(
    edges, vertices, plane=(0, 1), view=(-1, 1))
side_view = projection_simple.parallel(edges, vertices, plane=(2, 1))
side_view_b = projection_simple.parallel(
    edges, vertices, plane=(2, 1), view=(-1, 1))
perspec = projection_simple.perspective(edges, vertices)

# Front
camera_to_world = [[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]]

# Back
camera_to_world = [[-1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, -1, 0],
                   [0, 0, 0, 1]]
#  Right
# camera_to_world = [[-1.192093e-07, 0, 1, 0],
#                    [0, 1, 0, 0],
#                    [-1, 0, -1.192093e-07, 0],
#                    [0, 0, 0, 1]]

# Left
# camera_to_world = [[-1.192093e-07, 0, -1, 0],
#                    [0, 1, 0, 0],
#                    [1, 0, -1.192093e-07, 0],
#                    [0, 0, 0, 1]]

# Top
# camera_to_world = [[1, 0, 0, 0],
#                    [0, -1.192093e-07, -1, 0],
#                    [0, 1, -1.192093e-07, 0],
#                    [0, 0, 0, 1]]

# Bottom
# camera_to_world = [[1, 0, 0, 0],
#                    [0, -1.192093e-07, 1, 0],
#                    [0, -1, -1.192093e-07, 0],
#                    [0, 0, 0, 1]]
# Perspective
# camera_to_world = [[0.7071068, -0.5, -0.5, 0],
#                    [1.490116e-08, 0.7071068, -0.7071068, 0],
#                    [0.7071068, 0.5, 0.5, 0],
#                    [0, 0, 0, 1]]

# camera_to_world = [[0.870855, 0, -0.4915401, 1.342],
#                    [0, 1, 0, 0],
#                    [0.4915401, 0, 0.870855, -2.021],
#                    [0, 0, 0, 1]]
# camera_to_world = [[0.7478046, -0.2848986, -0.5996841, 1.894],
#                    [0.007423267, 0.9067805, -0.4215376, 1.62],
#                    [0.6638774, 0.3107762, 0.6802095, -2.021],
#                    [0, 0, 0, 1]]

# camera_to_world = [[0.871214, 0, -0.490904, 0],
#                    [-0.192902, 0.919559, -0.342346, 0],
#                    [0.451415, 0.392953, 0.801132, 0],
#                    [14.777467, 29.361945, 27.993464, 1]]

world_to_camera = utils.matrix_inverse(camera_to_world)

test_p = projection.vectices_to_space(vertices, world_to_camera)
# print(red_front_view)
# Render
# print("sur ", surfaces[0].edges)
# print(edges)

test_e = [] + surfaces[2].edges


result = hidden_line.surface_2d_hidden_line(
    surfaces[2].edges, vertices, surfaces[11])


result = hidden_line.get(test_p, surfaces)

test_e = result[0]

# for edge in surfaces[11].edges:
#     print(utils.edge_to_vertice(edge, vertices))

# print("hide")

# for edge in result[1]:
# print(utils.edge_to_vertice(edge, vertices))

render(result[1], test_p, scale=SCALE, position=(-50, -50), color="red")
render(test_e, test_p, scale=SCALE, position=(-50, -50))
# render(surfaces[11].edges, test_p, scale=SCALE,
#        position=(-50, -50), color="red")
# render(surfaces[5].edges, test_p, scale=SCALE, position=(-50, -50))
# render(edges, test_p, scale=SCALE, position=(-50, -50))

# render(edges, front_view, scale=SCALE, position=(-50, -50))
# render(edges, back_view, scale=SCALE, position=(-450, -50))
# render(edges, top_view, scale=SCALE, position=(-50, 150))
# render(edges, bottom_view, scale=SCALE, position=(-50, -150))
# render(edges, side_view, scale=SCALE, position=(-250, -50))
# render(edges, side_view_b, scale=SCALE, position=(150, -50))
# render(edges, perspec, scale=SCALE_3d,
#        position=(-WINDOW_WIDTH / 2 + 100, - WINDOW_HEIGHT / 2 + 50))

p = perspec
p = projection.normalized_device(p)
p = projection.to_raster_space(p, 1024 - 1, 1024 - 1)
edges = [(1, 5), (5, 7), (7, 3), (3, 1), (4, 3), (3, 7), (7, 8), (8, 4), (8, 7), (7, 5), (5, 6), (6, 8),
         (6, 2), (2, 4), (4, 8), (8, 6), (2, 1), (1, 3), (3, 4), (4, 2), (6, 5), (5, 1), (1, 2), (2, 6)]
# print(p)
# p = rd.get_2d_view(edges, p)
# rd.render(1024, 1024, p).save("result.png")

# [(511, 1023), (511, 682), (1023, 682), (1023, 341), (0, 682), (0, 341), (511, 341), (511, 0)]

# print(p)

# test_p = [(0, 682), (500, 682), (512, 512)]
# test_p = projection.normalized_device(test_p)
# CAN_W = 100
# CAN_H = 100
# test_p = projection.to_raster_space(test_p, CAN_W - 1, CAN_H - 1)
# print(test_p)
# test_p = rd.get_2d_view([(1, 2)],  test_p)
# rd.render(CAN_W, CAN_H, test_p).save("result.png")

input("Press any key to exit... ")
