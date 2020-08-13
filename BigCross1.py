def BigCross1(M, m):
    max_center = [-1, -1]
    max_length = 0
    for i in range(m):
        for j in range(m):
            if M[i][j] == 1:
                cur_length = CheckCenter1(M, [i, j])
                if cur_length > max_length:
                    max_center = [i, j]
                    max_length = cur_length
    if -1 in max_center:
        print("No cross was found")
        return [-1, -1], 0
    else:
        # if index starts with 1:
        max_center[0] += 1
        max_center[1] += 1
        print("Cross found at {0} and it's longest branch is {1}".format(max_center, max_length))
        return max_center, max_length


def CheckCenter1(M, center):
    distance = 1
    length = 0
    # if can make at least one step, check how many steps can be made
    hor_valid = Cover1(M, center, distance, "horizontal")
    ver_valid = Cover1(M, center, distance, "vertical")

    if hor_valid and ver_valid:
        # TODO: delete prints

        distance += 1
        while hor_valid or ver_valid:
            if hor_valid:
                # if center == [6, 3]:
                   # print("checking horizontal distance {0}".format(distance))
                   # print("*")
                   # print("result is {0}".format(Cover1(M, center, distance, "horizontal")))
                if not Cover1(M, center, distance, "horizontal"):
                    hor_valid = False
            if ver_valid:
                # if center == [6, 3]:
                    # print("checking vertical distance {0}".format(distance))
                    # print("*")
                    # print("result is {0}".format(Cover1(M, center, distance, "vertical")))
                if not Cover1(M, center, distance, "vertical"):
                    ver_valid = False
            distance += 1
            length += 1
    return length


def Cover1(M, center, distance, direction):
    if direction == "horizontal":
        # if center == [6, 3]:
            # print("left: {0} right: {1} left value: {2} right value: {3} {4}".format(center[1] - distance, center[1] + distance))
        if (center[1] - distance >= 0) and (center[1] + distance < len(M)):
            if (M[center[0]][center[1] - distance] == 1 and
                    M[center[0]][center[1] + distance] == 1):
                return True
    if direction == "vertical":
        if (center[0] - distance >= 0) and (center[0] + distance < len(M)):
            if (M[center[0] - distance][center[1]] == 1 and
                    M[center[0] + distance][center[1]] == 1):
                return True
    return False
