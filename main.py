
from model import read_model, move_model_to_first_quadrant
from render_turtle import render_2d, render_3d
from projection import vectices_to_space, world_space_to_camera_space, normalized_device, to_raster_space

# Configuration
MODEL_FILE = "models/cube_long.obj"
GRID_SIZE = 1
MIN_POINT = (0, 0)
MAX_POINT = (300, 300)
BOARD_SIZE = (MAX_POINT[0] - MIN_POINT[0], MAX_POINT[1] - MIN_POINT[1])
SCALE = 20


vertices = []
edges = []
read_model(MODEL_FILE, edges, vertices)
render_2d([], edges, vertices, (0, 2), (-200, 200), SCALE, True)
render_2d([], edges, vertices, (0, 1), (-200, -200), SCALE)
render_2d([], edges, vertices, (2, 1), (150, -200), SCALE, False, True)
render_3d([], edges, vertices, scale=SCALE/2, offset=(150, 150))

input("Press any key to exit... ")
