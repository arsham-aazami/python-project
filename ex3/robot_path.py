coordinate = [0, 0]

def distance(direction_list):
    # implementing the location that robot can go (calculating the distance from the origin )
    for direction in direction_list:
        if direction == 'n':
            coordinate[0] += 1
        elif direction == 's':
            coordinate[0] -= 1
        elif direction == 'e':
            coordinate[1] += 1
        elif direction == 'w':
            coordinate[1] -= 1
    return coordinate


def robot_path(direction_list):

    robot_default_dir = [
            ["e", "n", "e", "e", "n"],
            ["w", "n", "w", "n", "w", "w", "n"]
    ]
    dis_location1 = distance(robot_default_dir[0])
    dis_location2 = distance(robot_default_dir[0])
    dis_arbitrary_location = distance(direction_list)
    if dis_arbitrary_location == dis_location1 or dis_arbitrary_location == dis_location2:
        return True
    else:
        return False


robot_path(['e', 'e', 'n', 'w', 'n'])