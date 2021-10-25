# Generative art examples
# Copyright Martin McBride 2021
# MIT licence

from generativepy.drawing import make_image, setup
from generativepy.color import Color
from generativepy.geometry import Square

import random
import math

'''
Repeated squares
'''

def draw1(ctx, width, height, frame_no, frame_count):
    setup(ctx, width, height, width=11, background=Color(1))

    for i in range(1, 11):
        for j in range(1, 11):
            ctx.save()
            ctx.translate(i, j)
            Square(ctx).of_corner_size((-0.4, -0.4), 0.8).fill(Color(1, 0.3, 0.5))
            ctx.restore()

make_image("simple-shapes-repeated-squares.png", draw1, 500, 500)

'''
Random colours
'''

colors = [
    Color.of_hsl(0, 0.5, 0.25),
    Color.of_hsl(0, 0.5, 0.5),
    Color.of_hsl(0, 0.5, 0.75),
    Color.of_hsl(0.33, 0.5, 0.25),
    Color.of_hsl(0.33, 0.5, 0.5),
    Color.of_hsl(0.33, 0.5, 0.75),
    Color.of_hsl(0.66, 0.5, 0.25),
    Color.of_hsl(0.66, 0.5, 0.5),
    Color.of_hsl(0.66, 0.5, 0.75),
]

def draw2(ctx, width, height, frame_no, frame_count):
    setup(ctx, width, height, width=11, background=Color(1))

    for i in range(1, 11):
        for j in range(1, 11):
            ctx.save()
            ctx.translate(i, j)
            color = random.choice(colors)
            Square(ctx).of_corner_size((-0.4, -0.4), 0.8).fill(color)
            ctx.restore()

make_image("simple-shapes-random-colours.png", draw2, 500, 500)

'''
Size depends on position
'''

def get_radius(x, y):
    return math.fabs(math.sin(x/2) + math.cos(y/4))/8 + .2

def draw3(ctx, width, height, frame_no, frame_count):
    setup(ctx, width, height, width=11, background=Color(1))

    for i in range(1, 11):
        for j in range(1, 11):
            ctx.save()
            ctx.translate(i, j)
            radius = get_radius(i, j)
            Square(ctx).of_corner_size((-radius, -radius), 2*radius).fill(Color(1, 0.3, 0.5))
            ctx.restore()

make_image("simple-shapes-varying-size.png", draw3, 500, 500)

'''
Size depends on position
'''

def get_rotation(x, y):
    return (x%3)/3 + (y%4)/2

def draw4(ctx, width, height, frame_no, frame_count):
    setup(ctx, width, height, width=11, background=Color(1))

    for i in range(1, 11):
        for j in range(1, 11):
            ctx.save()
            ctx.translate(i, j)
            ctx.rotate(get_rotation(i, j))
            Square(ctx).of_corner_size((-.4, -.5), 0.8).fill(Color(1, 0.3, 0.5))
            ctx.restore()

make_image("simple-shapes-varying-rotation.png", draw4, 500, 500)

'''
Vary everything
'''

def draw5(ctx, width, height, frame_no, frame_count):
    setup(ctx, width, height, width=11, background=Color(1))

    for i in range(1, 11):
        for j in range(1, 11):
            ctx.save()
            ctx.translate(i, j)
            ctx.rotate(get_rotation(i, j))
            radius = get_radius(i, j)
            color = random.choice(colors)
            Square(ctx).of_corner_size((-radius, -radius), 2*radius).fill(color)
            ctx.restore()

make_image("simple-shapes-varying-all.png", draw5, 500, 500)

