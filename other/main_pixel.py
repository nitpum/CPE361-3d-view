
# def draw_edge(edges, vertices):
#     wn = turtle.Screen()
#     t = turtle.Turtle()
#     t.speed(0)
#     t.pensize(1)
#     t.hideturtle()
#     wn.tracer(0, 0)
#     t.penup()

#     for edge in edges:
#           t.penup()

#           from_edge = edge[0] - 1
#           to_edge = edge[1] - 1
#           p = vertices[from_edge]

#           x_2d = p[plane[0]]
#           y_2d = p[plane[1]]
#           if filp:
#               y_2d *= -1
#           if mirror:
#               x_2d *= -1
#           x_2d = x_2d * scale + offset[0]
#           y_2d = y_2d * scale + offset[1]
#           t.goto(x_2d, y_2d)

#           p = vertices[to_edge]
#           t.pendown()
#           x_2d = p[plane[0]]
#           y_2d = p[plane[1]]
#           if filp:
#               y_2d *= -1
#           if mirror:
#               x_2d *= -1
#           x_2d = x_2d * scale + offset[0]
#           y_2d = y_2d * scale + offset[1]
#           t.goto(x_2d, y_2d)

#       wn.update()

# print(vertices[1][1] - vertices[0][1] / vertices[1][0] - vertices[0][0])

# world_to_camera = [[0.718762, 0.615033, -0.324214, 0],
#                    [-0.393732, 0.744416, 0.539277, 0],
#                    [0.573024, -0.259959, 0.777216, 0],
#                    [0.526967, 1.254234, -2.53215, 1]]
# world_to_camera = [[0.871214, 0, -0.490904, 0],
#                    [-0.192902, 0.919559, -0.342346, 0],
#                    [0.451415, 0.392953, 0.801132, 0],
#                    [14.777467, 29.361945, 27.993464, 1]]

# world_to_camera = inv(np.array(world_to_camera))

# perspective = vectices_to_space(vertices, world_to_camera)

# for i in range(len(perspective)):
#     perspective[i] = (int(perspective[i][0]), int(
#         perspective[i][1]), int(perspective[i][2]))

# # print(perspective)
# screen = world_space_to_camera_space(perspective)
# # print(screen)
# norm = normalized_device(screen, 2, 2)
# raster = to_raster_space(norm, 512, 512)
# print(raster)
# camera([], edges, raster, plane=(0, 1),
#        scale=1, offset=(-150, -150))


# points_2d = get_2d_view(edges, vertices, plane=(0, 1), scale=1)
# render(10, 10, points_2d).save("result.png")

# print(vectices_to_space(vertices, [[0.718762, 0.615033, -0.324214, 0],
#                                    [-0.393732, 0.744416, 0.539277, 0],
#                                    [0.573024, -0.259959, 0.777216, 0],
#                                    [0.526967, 1.254234, -2.53215, 1]]))
