from turtle import *
def draw_koch_curve(length, depth):
    if depth == 0:
        forward(length)
    else:
        draw_koch_curve(length / 3, depth - 1)
        left(60)
        draw_koch_curve(length / 3, depth - 1)
        right(120)
        draw_koch_curve(length / 3, depth - 1)
        left(60)
        draw_koch_curve(length / 3, depth - 1)

def draw_koch_flake(length, depth):
    draw_koch_curve(length, depth)
    right(120)
    draw_koch_curve(length, depth)
    right(120)
    draw_koch_curve(length, depth)

# draw_koch_curve(300, 3)
draw_koch_flake(300, 2)
input()