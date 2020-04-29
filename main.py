
import turtle
from model import read_model, move_model_to_first_quadrant
from render_turtle import render
import projection_simple
# Configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MODEL_FILE = "models/cube_long.obj"
GRID_SIZE = 1
MIN_POINT = (0, 0)
MAX_POINT = (300, 300)
BOARD_SIZE = (MAX_POINT[0] - MIN_POINT[0], MAX_POINT[1] - MIN_POINT[1])
SCALE = (30, 30)
SCALE_3d = (20, 20)

wn = turtle.Screen()
wn.setup(WINDOW_WIDTH, WINDOW_HEIGHT)


vertices = []
edges = []
read_model(MODEL_FILE, edges, vertices)

# Projection
top_view = projection_simple.parallel(edges, vertices, plane=(0, 2))
front_view = projection_simple.parallel(edges, vertices, plane=(1, 2))
side_view = projection_simple.parallel(edges, vertices, plane=(2, 1))
perspec = projection_simple.perspective(edges, vertices)
# Render
render(edges, top_view, scale=SCALE,
       position=(-WINDOW_WIDTH / 2, 0), offset=(100, 100))
render(edges, front_view, scale=SCALE,
       position=(-WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2 + 20), offset=(100, 100))
render(edges, side_view, scale=SCALE, position=(
    0, -WINDOW_HEIGHT / 2 + 20), offset=(100, 100))
render(edges, perspec, scale=SCALE_3d)

input("Press any key to exit... ")
