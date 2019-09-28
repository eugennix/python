import turtle as t

def draw_GaussX(l, n):
    if n == 0:
        t.forward(l)
        return
    x = l / 3
    draw_GaussX(x, n - 1)
    y = x/1.1
    t.penup()
    t.forward(x/2)
    t.right(90)
    t.forward(y)
    t.pendown()
    t.left(180)
    draw_GaussX(2*y, n-1)
    t.penup()
    t.backward(y)
    t.right(90)
    t.forward(x/2)
    t.pendown()
    draw_GaussX(x, n - 1)

def draw_Gauss(l, n):
    if n == 0:
        t.forward(l)
        return
    x = l / 3
    draw_Gauss(x, n - 1)
    t.penup()
    t.forward(x)
    t.pendown()
    draw_Gauss(x, n - 1)

t.speed('fastest')

t.penup()
t.goto(-350, 250)
t.pendown()

draw_Gauss(600, 6)
for i in range(4):
    # draw_GaussX(600, 5)
    t.right(90)



i = input()