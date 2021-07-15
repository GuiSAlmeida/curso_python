from enum import Enum


class Directions(Enum):
    right = 0
    left = 1
    up = 2
    down = 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name} to position {direction.value}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.up))

    for directory in Directions:
        print(directory, directory.name, directory.value)

