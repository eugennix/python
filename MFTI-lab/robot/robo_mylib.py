
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

def go_up(st=100, fill=False):
    while st and not wall_is_above():
        if fill: fill_cell()
        move_up()
        st -= 1
        if fill: fill_cell()


def go_down(st=100, fill=False):
    while st and not wall_is_beneath():
        if fill: fill_cell()
        move_down()
        st -= 1
        if fill: fill_cell()


def go_left(st=100, fill=False):
    while st and not wall_is_on_the_left():
        if fill: fill_cell()
        move_left()
        st -= 1
    if fill: fill_cell()

def go_right(st=100, fill=False):
    while st and not wall_is_on_the_right():
        if fill: fill_cell()
        move_right()
        st -= 1
    if fill: fill_cell()


def paint_cros3():
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

def try_down(st):
    made_st, i = 0, st
    while i:
        if not wall_is_beneath():
            move_down()
            made_st += 1
        i -= 1
    if made_st != st:
        while made_st:
            move_up()
            made_st -= 1
        return False
    else:
        return True
