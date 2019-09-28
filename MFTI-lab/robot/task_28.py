#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    count_filled = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            count_filled += 1
            if count_filled == 5:
                break
        move_right()


if __name__ == '__main__':
    run_tasks()
