#!/usr/bin/python3

from pyrob.api import *

def paint_down():
    steps = 0
    while not wall_is_beneath():
        fill_cell()
        move_down()
        steps += 1
    return steps

def go_up(st):
    while st:
        move_up()
        st -= 1

def go_left():
    while not wall_is_on_the_left():
        move_left()

@task(delay=0.02)
def task_4_11():
    move_down()
    move_right()
    while True:
        st = paint_down() - 1
        move_right()
        if wall_is_on_the_right():
            break
        go_up(st)
    go_left()
    move_right()



if __name__ == '__main__':
    run_tasks()
