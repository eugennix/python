import turtle as t


def kvadrat(d):
    ''' черепаха - Квадрат со стороной == d
        начало -> Ч - левый верхний угол,
        конец - > Ч на прежнем месте
    '''
    for i in range(4):
        t.forward(d)
        t.right(90)


def treugolnik(d):
    ''' черепаха - треугольник со стороной == d
        начало -> Ч - левый верхний угол, рисуен направо
        конец - > Ч на прежнем месте
    '''
    t.forward(d)
    t.right(120)
    t.forward(d)
    t.right(120)
    t.forward(d)
    t.right(120)


def na_prohode(d, f):
    ''' черепаха - рисует фигуру figure, прямо перед собой
        начало -> Ч
        конец - > прошла фигуру, стоит с другой стороны
    '''
    t.penup()
    t.left(90)
    t.forward(d / 2)
    t.right(90)
    t.pendown()
    f(d)
    t.penup()
    t.right(90)
    t.forward(d / 2)
    t.left(90)


def rotor(f, angle=0):
    ''' черепаха - рисует фигуру figure, вращая на угол по часовой
        начало -> Ч
        конец - > на том же месте
    '''

    def x(d, *args):
        t.penup()
        r = d / 2 * 2 ** 0.5
        t.right(45)
        t.forward(r)
        t.right(angle)
        t.backward(r)
        t.left(45)
        t.pendown()
        f(d, *args)
        t.penup()
        t.right(45)
        t.forward(r)
        t.left(angle)
        t.backward(r)
        t.left(45)

    return x


def scale(f, M=1):
    ''' черепаха - рисует фигуру figure, масштабируя
        начало -> Ч
        конец - > на том же месте
    '''

    def x(d, *args):
        t.penup()
        r = d / 2 * 2 ** 0.5
        t.right(45)
        t.forward(r)
        t.backward(d / 2 * M * 2 ** 0.5)
        t.left(45)
        t.pendown()
        f(d * M, *args)
        t.penup()
        t.right(45)
        t.forward(d / 2 * M * 2 ** 0.5)
        t.backward(r)
        t.left(45)

    return x


def line_of_fig(figure, l, N, zazor=0, krai=0):
    ''' черепаха - линию из N фигур figure,
        между ними зазор, и с краёв тоже пустое место
        начало -> Ч
        конец - > в конце линии, прошла расстояние d
    '''
    t.penup()
    t.forward(krai)
    d = (l - 2 * krai - (N - 1) * zazor) / N
    for i in range(N):
        na_prohode(d, figure)
        t.forward(d)
        if i < N - 1:
            t.forward(zazor)
    t.forward(krai)


def cross3(d):
    t.penup()
    t.forward(d / 3)
    t.pendown()
    for i in range(4):
        t.forward(d / 3)
        t.right(90)
        t.forward(d / 3)
        t.left(90)
        t.forward(d / 3)
        t.right(90)
    t.penup()
    t.backward(d / 3)


def swiss(d):
    kvadrat(d)
    t.penup()
    t.right(45)
    t.forward(d / 5)
    t.left(45)
    t.pendown()
    cross3(2 * d / 3)
    t.penup()
    t.right(45)
    t.backward(d / 5)
    t.left(45)


def kv2(d):
    rotor(kvadrat, 45)(d)
    t.pendown()
    kvadrat(d)
    t.penup()
    scale(kvadrat, 1.5)(d)
    scale(cross3, 0.5)(d)
    rotor(kvadrat, 45)(d)


def line_of_figs_list(figure_list, l, N, zazor=0, krai=0):
    ''' черепаха - линию из N фигур из figure_list,
        повторяя их циклически
        между ними зазор, и с краёв тоже пустое место
        начало -> Ч
        конец - > в конце линии, прошла расстояние l
    '''
    t.penup()
    t.forward(krai)
    d = (l - 2 * krai - (N - 1) * zazor) / N
    count = 0
    for i in range(N):
        na_prohode(d, figure_list[count])
        count += 1
        count %= len(figure_list)
        t.forward(d)
        if i < N - 1:
            t.forward(zazor)
    t.forward(krai)


def line_of_uzor(uzor_list, l, width, start_end_list=None, uzor=True):
    ''' черепаха - линию из узорных фигур шириной w из usor_list,
        повторяя их циклически
        если uzor = True, то Ч не смещается после каждого шага
        фигуры особого типа, Ч начинает с середины левой части,
        заканчивает справа в середине
        uzor=False - обычные фигуры
        начало -> Ч
        конец - > в конце линии, прошла расстояние l
    '''
    N = l // width
    count = 0
    if start_end_list:
        t.penup()
        t.backward(width / 2)
        t.left(90)
        t.forward(width / 2)
        t.right(90)
        t.pendown()
        start_end_list[0](width)
        t.penup()
        t.forward(width)
        t.right(90)
        t.forward(width / 2)
        t.left(90)
        N -= 1
        t.pendown()
    for i in range(N):
        uzor_list[count](width)
        count += 1
        count %= len(uzor_list)
    if start_end_list:
        t.penup()
        t.left(90)
        t.forward(width / 2)
        t.right(90)
        t.pendown()
        start_end_list[1](width)
        t.penup()
        t.forward(width)
        t.right(90)
        t.forward(width / 2)
        t.left(90)
        t.backward(width/2)


def uzor1(d):
    t.pendown()
    t.forward(d / 4)
    t.right(90)
    t.forward(d / 2)
    t.left(90)
    t.forward(d / 2)
    t.left(90)
    t.forward(d / 2)
    t.right(90)
    t.forward(d / 4)



def uzor2(d):
    t.pendown()
    t.forward(d / 4)
    t.left(90)
    t.forward(d / 2)
    t.right(90)
    t.forward(d / 2)
    t.right(90)
    t.forward(d / 2)
    t.left(90)
    t.forward(d / 4)

def uzor3(d):
    t.pendown()
    t.forward(d / 4)
    t.right(60)
    t.forward(d / 2)
    t.left(120)
    t.forward(d / 2)
    t.right(60)
    t.forward(d / 4)

def uzor4(d):
    t.pendown()
    t.forward(d / 4)
    t.left(60)
    t.forward(d / 2)
    t.right(120)
    t.forward(d / 2)
    t.left(60)
    t.forward(d / 4)

