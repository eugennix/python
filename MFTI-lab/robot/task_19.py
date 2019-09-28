#!/usr/bin/python3

from pyrob.api import *

def find_exit_above():
    if not wall_is_above():
        return
    while not wall_is_on_the_left():
        if not wall_is_above():
            return
        move_left()
    while not wall_is_on_the_right():
        if not wall_is_above():
            return
        move_right()


def go_top():
    while not wall_is_above():
        move_up()
def go_left():
    while not wall_is_on_the_left():
        move_left()
def go_right():
    while not wall_is_on_the_right():
        move_right()
def go_down():
    while not wall_is_beneatht():
        move_down()

@task
def task_8_29():
    find_exit_above()
    if not wall_is_above():
        go_top()
        go_left()
    else:
        go_right()

if __name__ == '__main__':
    run_tasks()
