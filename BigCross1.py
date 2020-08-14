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
    length = -1
    valid = Cover1(M, center, distance)
    while valid:
        valid = Cover1(M, center, distance)
        distance += 1
        length += 1
    return length


def Cover1(M, center, distance):
    if (center[1] - distance >= 0 and
            center[1] + distance < len(M) and
            center[0] - distance >= 0 and
            center[0] + distance < len(M)):
        if (M[center[0]][center[1] - distance] == 1 and
                M[center[0]][center[1] + distance] == 1 and
                M[center[0] - distance][center[1]] == 1 and
                M[center[0] + distance][center[1]] == 1):
            return True
    return False
