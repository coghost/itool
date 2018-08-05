# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/12 5:32 PM'
__description__ = '''
    ☰
  ☱   ☴
☲   ☯   ☵
  ☳   ☶
    ☷
'''

import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import urwid

from logzero import logger as log


class ViListBox(urwid.ListBox):
    # Catch key presses in box and pass them as arrow keys
    def keypress(self, size, key):
        if key == 'j':
            key = 'down'
        elif key == 'k':
            key = 'up'
        elif key == 'h':
            key = 'left'
        elif key == 'l':
            key = 'right'
        elif key == 'G':
            key = 'page down'
        elif key == 'g':
            key = 'page up'
        return super(ViListBox, self).keypress(size, key)


def radio_button(g, l, fn):
    """ Inheriting radio button of urwid """
    w = urwid.RadioButton(g, l, False, on_state_change=fn)
    w = urwid.AttrWrap(w, 'button normal', 'button select')
    return w


def button(t, fn, data=None):
    w = urwid.Button(t, fn, data)
    w = urwid.AttrWrap(w, 'button normal', 'button select')
    return w


if __name__ == '__main__':
    pass
