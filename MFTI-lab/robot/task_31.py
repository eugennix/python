#!/usr/bin/python3

from pyrob.api import *

def find_pass_down():
    while not wall_is_on_the_right():
        if not wall_is_beneath():
            move_down()
            return True
        move_right()
    while not wall_is_on_the_left():
        if not wall_is_beneath():
            move_down()
            return True
        move_left()



@task(delay=0.01)
def task_8_30():
    flag = True
    while flag:
        flag = find_pass_down()


if __name__ == '__main__':
    run_tasks()
