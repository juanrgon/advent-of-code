import os.path
from collections import Counter

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def main():
    print("Solution to Part 1: " + str(_part_1()))
    print("Solution to Part 2: " + str(_part_2()))


def _part_1():
    image = _input()
    layer_with_fewest_0s = []
    for layer in _chunked(image, IMAGE_HEIGHT * IMAGE_WIDTH):
        if not layer_with_fewest_0s:
            layer_with_fewest_0s = layer
        elif Counter(layer)['0'] < Counter(layer_with_fewest_0s)['0']:
            layer_with_fewest_0s = layer

    return Counter(layer_with_fewest_0s)['1'] * Counter(layer_with_fewest_0s)['2']


def _part_2():
    image = _input()
    return _image_decoded(image)


def _image_decoded(image):
    white_pixel = " "
    black_pixel = "*"

    final_layer = ["2"] * IMAGE_WIDTH * IMAGE_HEIGHT
    for layer in _chunked(image, IMAGE_HEIGHT * IMAGE_WIDTH):
        for i, pixel in enumerate(layer):
            if pixel != "2" and final_layer[i] == "2":
                final_layer[i] = pixel

    decoded = [black_pixel if pixel == "1" else white_pixel for pixel in final_layer]

    result = "\n"
    for row in _chunked(decoded, IMAGE_WIDTH):
        result += ("".join(row)) + "\n"

    return result


def _input():
    with open(os.path.join(os.path.dirname(__file__), "input")) as f:
        return f.read().strip()


def _chunked(array, n):
    return zip(*([iter(array)] * n))


if __name__ == "__main__":
    main()
