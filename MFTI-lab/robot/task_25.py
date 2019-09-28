#!/usr/bin/python3

from pyrob.api import *
import robo_mylib

def try_right(st):
    made_st, i = 0, st
    while i:
        if not wall_is_on_the_right():
            move_right()
            made_st += 1
        i -= 1
    if made_st != st:
        while made_st:
            move_left()
            made_st -= 1
        return False
    else:
        return True

@task
def task_2_2():
    flag = True
    move_down()
    while flag:
        robo_mylib.paint_cros3()
        flag = try_right(4)



if __name__ == '__main__':
    run_tasks()
