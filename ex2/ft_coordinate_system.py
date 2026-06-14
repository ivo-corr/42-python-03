#! /usr/bin/python3

def get_player_pos():
    while (True):
        try:
            coordinates = tuple(int(c) for c in input(
                "Enter new coordinates as floats in format"
                " 'x, y, z': ").split(","))
        except ValueError:
            print("Invalid syntax")
            continue
        if (len(coordinates) != 3):
            continue
        break
    return (coordinates)


if __name__ == "__main__":
    for c in get_player_pos():
        print(c)
