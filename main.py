
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

# Camera
# Front
camera_to_world_front = [[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]

# Back
camera_to_world_back = [[-1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, -1, 0],
                        [0, 0, 0, 1]]

# Top
camera_to_world_top = [[1, 0, 0, 0],
                       [0, -1.192093e-07, -1, 0],
                       [0, 1, -1.192093e-07, 0],
                       [0, 0, 0, 1]]

# Bottom
camera_to_world_bottom = [[1, 0, 0, 0],
                          [0, -1.192093e-07, 1, 0],
                          [0, -1, -1.192093e-07, 0],
                          [0, 0, 0, 1]]
#  Right
camera_to_world_right = [[-1.192093e-07, 0, 1, 0],
                         [0, 1, 0, 0],
                         [-1, 0, -1.192093e-07, 0],
                         [0, 0, 0, 1]]

# Left
camera_to_world_left = [[-1.192093e-07, 0, -1, 0],
                        [0, 1, 0, 0],
                        [1, 0, -1.192093e-07, 0],
                        [0, 0, 0, 1]]


# Perspective
camera_to_world_persp = [[0.7071068, -0.5, -0.5, 0],
                         [1.490116e-08, 0.7071068, -0.7071068, 0],
                         [0.7071068, 0.5, 0.5, 0],
                         [0, 0, 0, 1]]

# Projection
world_to_camera = utils.matrix_inverse(camera_to_world_front)
front_vertices = projection.vectices_to_space(vertices, world_to_camera)

world_to_camera = utils.matrix_inverse(camera_to_world_back)
back_vertices = projection.vectices_to_space(vertices, world_to_camera)

world_to_camera = utils.matrix_inverse(camera_to_world_top)
top_vertices = projection.vectices_to_space(vertices, world_to_camera)

world_to_camera = utils.matrix_inverse(camera_to_world_bottom)
bottom_vertices = projection.vectices_to_space(vertices, world_to_camera)

world_to_camera = utils.matrix_inverse(camera_to_world_right)
right_vertices = projection.vectices_to_space(vertices, world_to_camera)

world_to_camera = utils.matrix_inverse(camera_to_world_left)
left_vertices = projection.vectices_to_space(vertices, world_to_camera)

world_to_camera = utils.matrix_inverse(camera_to_world_persp)
persp_vertices = projection.vectices_to_space(vertices, world_to_camera)

# Hidden line
front_edges = hidden_line.get(front_vertices, surfaces)
back_edges = hidden_line.get(back_vertices, surfaces)
top_edges = hidden_line.get(top_vertices, surfaces)
bottom_edges = hidden_line.get(bottom_vertices, surfaces)
right_edges = hidden_line.get(right_vertices, surfaces)
left_edges = hidden_line.get(left_vertices, surfaces)

# Render
render(front_edges[1], front_vertices, scale=SCALE,
       position=(-50, -50), color="red")
render(front_edges[0], front_vertices, scale=SCALE, position=(-50, -50))

render(back_edges[1], back_vertices, scale=SCALE,
       position=(-450, -50), color="red")
render(back_edges[0], back_vertices, scale=SCALE, position=(-450, -50))

render(top_edges[1], top_vertices, scale=SCALE,
       position=(-50, 150), color="red")
render(top_edges[0], top_vertices, scale=SCALE, position=(-50, 150))

render(bottom_edges[1], bottom_vertices, scale=SCALE,
       position=(-50, -250), color="red")
render(bottom_edges[0], bottom_vertices, scale=SCALE, position=(-50, -250))

render(right_edges[1], right_vertices, scale=SCALE,
       position=(-250, -50), color="red")
render(right_edges[0], right_vertices, scale=SCALE, position=(-250, -50))

render(left_edges[1], left_vertices, scale=SCALE,
       position=(150, -50), color="red")
render(left_edges[0], left_vertices, scale=SCALE, position=(150, -50))

persp_vertices = utils.rotate(persp_vertices, -35)
render(edges, persp_vertices, scale=SCALE, position=(-450, -250))


input("Press any key to exit... ")
