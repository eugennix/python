#!/usr/bin/python3

from pyrob.api import *
import robo_mylib

def paint_cross3():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_up()

@task
def task_2_1():
    move_right()
    move_down()
    robo_mylib.paint_cros3()



if __name__ == '__main__':
    run_tasks()
