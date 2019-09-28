#!/usr/bin/python3

from pyrob.api import *

def find_exit_above():
    if not wall_is_above():
        return
    while not wall_is_on_the_right():
        if not wall_is_above():
            return
        move_right()

    while not wall_is_on_the_left():
        if not wall_is_above():
            return
        move_left()

def go_top():
    while not wall_is_above():
        move_up()
def go_left():
    while not wall_is_on_the_left():
        move_left()


@task
def task_8_28():
    find_exit_above()
    go_top()
    go_left()

if __name__ == '__main__':
    run_tasks()
