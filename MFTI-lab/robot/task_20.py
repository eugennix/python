#!/usr/bin/python3

from pyrob.api import *

def pain_left():
    while not wall_is_on_the_left():
        move_left()
        if not wall_is_on_the_left():
            fill_cell()

def pain_right():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_on_the_right():
            fill_cell()

def is_last_line():
    if wall_is_beneath():
        return True
    else:
        move_down()
        if wall_is_beneath():
            move_up()
            return True
        else:
            move_down()
            if wall_is_beneath():
                move_up()
                move_up()
                return True
            else:
                move_up()
                move_up()
                return False
def go_left():
    while not wall_is_on_the_left():
        move_left()

@task(delay=0.03)
def task_4_3():
    while not wall_is_beneath() and not is_last_line():
        pain_right()
        if is_last_line():
            break
        move_down()
        pain_left()
        move_down()
    go_left()
    move_right()


if __name__ == '__main__':
    run_tasks()
