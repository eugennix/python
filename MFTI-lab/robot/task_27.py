#!/usr/bin/python3

from pyrob.api import *
import robo_mylib

@task
def task_7_5():
    move_right()
    fill_cell()
    flag, step = True, 1
    while flag:
        if not wall_is_on_the_right():
            fill_cell()
        flag = robo_mylib.try_right(step)
        step += 1
    robo_mylib.go_right()



if __name__ == '__main__':
    run_tasks()
