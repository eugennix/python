#!/usr/bin/python3

from pyrob.api import *
import robo_mylib


@task
def task_5_10():
    while not wall_is_beneath():
        robo_mylib.go_right(fill=True)
        if not wall_is_beneath():
            move_down()
            robo_mylib.go_left(fill=True)
            if not wall_is_beneath():
                move_down()
    robo_mylib.go_right(fill=True)
    robo_mylib.go_left(fill=True)


if __name__ == '__main__':
    run_tasks()
