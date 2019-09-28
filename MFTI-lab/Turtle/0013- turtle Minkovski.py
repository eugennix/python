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

def draw_Minkovski(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l / 4
    draw_Minkovski(x, n - 1) #1
    turtle.left(90)
    draw_Minkovski(x, n - 1) #2
    turtle.right(90)
    draw_Minkovski(x, n - 1) #3
    turtle.right(90)
    draw_Minkovski(x, n - 1) #4

    draw_Minkovski(x, n - 1) #5
    turtle.left(90)
    draw_Minkovski(x, n - 1) #6
    turtle.left(90)
    draw_Minkovski(x, n - 1) #7
    turtle.right(90)
    draw_Minkovski(x, n - 1) #8

def kv_Minkovski(l, n):
    for i in range(4):
        draw_Minkovski(l, n)
        turtle.right(90)

def Minkovski3():
    turtle.penup()
    turtle.goto(-500, 200)
    turtle.goto(-350, 200)
    turtle.pendown()
    turtle.color('red')
    kv_Minkovski(500, 1)
    turtle.color('green')
    kv_Minkovski(500, 2)
    turtle.color('blue')
    kv_Minkovski(500, 3)



# draw_Koch(800, 5)
turtle.speed('fastest')

turtle.penup()
turtle.goto(-500, 200)
turtle.goto(-350, 200)
turtle.pendown()

# Koch_triang(500, 4)
draw_Minkovski(1024, 4)
# Minkovski3()

i = input()