#!/usr/bin/python3

from pyrob.api import *
import robo_mylib

def cross_line():
    flag = True
    while flag:
        robo_mylib.paint_cros3()
        flag = robo_mylib.try_right(4)


@task(delay=0.01)
def task_2_4():
    flag = True
    while flag:
        cross_line()
        robo_mylib.go_left()
        flag = robo_mylib.try_down(4)





if __name__ == '__main__':
    run_tasks()
