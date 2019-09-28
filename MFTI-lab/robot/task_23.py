#!/usr/bin/python3

from pyrob.api import *
import robo_mylib

@task(delay=0.03)
def task_6_6():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            move_up()
            fill_cell()
            robo_mylib.go_up(fill=True)
            robo_mylib.go_down()
    while wall_is_beneath():
        move_left()


if __name__ == '__main__':
    run_tasks()
