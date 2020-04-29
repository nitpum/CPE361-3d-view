from PIL import Image


def get_max_y(points):
    max_y = points[0][1]
    for point in points:
        if point[1] > max_y:
            max_y = point[1]
    return max_y


def get_min_y(points):
    min_y = points[0][1]
    for point in points:
        if point[1] < min_y:
            min_y = point[1]
    return min_y


def translate(points, to):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][0] + to[0], points[i][1] + to[1])
    return result


def mirror(points):
    result = [] + points
    for i in range(len(points)):
        result[i] = (-points[i][0], points[i][1])
    return result


def swap_x(points):
    result = [] + points
    for i in range(len(points)):
        result[len(points) - 1 - i] = (points[i][0], points[i][1])
    return result


def swap_y(points):
    result = [] + points
    y_max = get_max_y(result)
    y_min = get_min_y(result)
    result = [] + translate(result, (0, -y_max))
    result = [] + flip(result)
    result = [] + translate(result, (0, y_min))
    return result


def flip(points):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][0], -points[i][1])
    return result


def flip45(points):
    result = [] + points
    for i in range(len(points)):
        result[i] = (points[i][1], points[i][0])
    return result


def mid_point_alogirthm(x1, y1, x2, y2):
    points = []
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dU = 2 * (dy - dx)
    dD = 2 * dy
    x = x1
    y = y1
    while x <= x2:
        points.append((x, y))
        if d > 0:
            d = d + dU
            x += 1
            y += 1
        else:
            d = d + dD
            x += 1
    return points


def draw_line(x1, y1, x2, y2):
    result = [(x1, y1), (x2, y2)]

    swapped_x = False
    swapped_y = False
    flipped45 = False

    if result[0][0] > result[1][0]:
        swapped_x = True
        result = [] + swap_x(result)
    if result[0][1] > result[1][1]:
        swapped_y = True
        result = [] + swap_y(result)
    if result[1][1] > result[1][0]:
        flipped45 = True
        result = [] + flip45(result)

    # print(swapped_x, swapped_y, flipped45)

    result = mid_point_alogirthm(
        result[0][0], result[0][1], result[1][0], result[1][1])

    if flipped45:
        result = [] + flip45(result)
    if swapped_y:
        result = [] + swap_y(result)
    if swapped_x:
        result = [] + swap_x(result)

    return result


def render(width, height, points):
    img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), (255, 255, 255, 255))

    for point in points:
        img.putpixel(
            (point[0], height - 1 - point[1]), (0, 0, 0, 255))

    return img
