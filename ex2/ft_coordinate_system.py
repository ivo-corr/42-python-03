#! /usr/bin/python3

import math

def get_player_pos():
    while (True):
        try:
            coordinates = tuple(float(c) for c in input(
                "Enter new coordinates as floats in format"
                " 'x, y, z': ").split(","))
        except ValueError:
            print("Invalid syntax")
            continue
        if (len(coordinates) != 3):
            continue
        break
    return (coordinates)


def calc_distance(point_one: tuple[int, int, int],
                  point_two: tuple[int, int, int]) -> float:
    return (round(math.sqrt(
        pow((point_one[0] - point_two[0]), 2) +
        pow((point_one[1] - point_two[1]), 2) +
        pow((point_one[2] - point_two[2]), 2)
        ), 4))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={coordinates[0]},"
          f"Y={coordinates[1]},"
          f"Z={coordinates[2]}")
    print(f"Distance to center: {calc_distance(coordinates, (0, 0, 0))}\n")
    print("Get a second set of coordinates")
    coordinates_two = get_player_pos()
    print("Distance between the 2 sets of coordinates:"
          f"{calc_distance(coordinates, coordinates_two)}")
