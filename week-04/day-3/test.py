import random
import webcolors


def rgb():
    hex_color = 0
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0, 255))

    print(webcolors.rgb_to_hex(rgb))



rgb()