import turtle

def draw_Koch(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l / 3
    draw_Koch(x, n - 1)

    turtle.left(60)
    draw_Koch(x, n - 1)

    turtle.right(120)
    draw_Koch(x, n - 1)

    turtle.left(60)
    draw_Koch(x, n - 1)

def Koch_triang(d, n):
    for i in range(3):
        draw_Koch(d, n)
        turtle.right(120)


# draw_Koch(800, 5)
turtle.speed('fastest')
turtle.penup()
turtle.left(155)
turtle.forward(400)
turtle.pendown()
turtle.right(155)
Koch_triang(500, 4)

i = input()