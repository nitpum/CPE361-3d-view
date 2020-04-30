def dot(p0, p1):
    return p0[0] * p1[0] + p0[1] * p1[1]


def max(t):
    maximum = -2147483648
    for i in range(len(t)):
        if t[i] > maximum:
            maximum = t[i]
    return maximum


def min(t):
    minimum = 2147483648
    for i in range(len(t)):
        if t[i] < minimum:
            minimum = t[i]
    return minimum


def cyrus_beck(vertices, line):
    # print(vertices)
    new_pair = []
    normal = []
    n = len(vertices)
    for i in range(len(vertices)):
        second = vertices[(i + 1) % n][0] - vertices[i][0]
        first = vertices[i][1] - vertices[(i + 1) % n][1]
        norm = [first, second]
        normal.append(norm)

    p1_p0 = (line[1][0] - line[0][0], line[1][1] - line[0][1])

    p0_pei = []
    for i in range(n):
        new_p0_pe = (vertices[i][0] - line[0][0], vertices[i][1] - line[0][1])
        p0_pei.append(new_p0_pe)

    numerator = []
    denominator = []

    for i in range(n):
        numerator.append(dot(normal[i], p0_pei[i]))
        denominator.append(dot(normal[i], p1_p0))

    t = []
    t_e = []
    t_l = []

    for i in range(n):
        if denominator[i] == 0:
            t.append(float(numerator[i]))
        else:
            t.append(float(numerator[i]) / float(denominator[i]))

        if denominator[i] > 0:
            t_e.append(t[i])
        else:
            t_l.append(t[i])

    temp = [0, 0]
    t_e.append(float(0))
    temp[0] = max(t_e)

    t_l.append(float(1))
    temp[1] = min(t_l)

    if temp[0] > temp[1]:
        new_pair.append((-1, -1))
        new_pair.append((-1, -1))
        return new_pair

    first = float(line[0][0]) + float(p1_p0[0]) * float(temp[0])
    second = float(line[0][1] + float(p1_p0[1]) * float(temp[0]))
    new_pair.append((first, second))
    first = float(line[0][0]) + float(p1_p0[0]) * float(temp[1])
    second = float(line[0][1] + float(p1_p0[1]) * float(temp[1]))
    new_pair.append((first, second))
    return new_pair


# result = cyrus_beck([(200, 50),
#                      (250, 100),
#                      (200, 150),
#                      (100, 150),
#                      (50, 100),
#                      (100, 50)], [(10, 10), (450, 200)])
# print(result)
