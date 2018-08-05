#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lihe <imanux@sina.com>'
__date__ = '2018/6/12 6:04 PM'
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


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


preset_palette = [
    ('body', 'default', 'default', 'standout'),
    ('header', 'default', 'dark red',),
    ('screen edge', 'light blue', 'brown'),
    ('main shadow', 'dark gray', 'black'),
    ('line', 'default', 'light gray', 'standout'),
    ('menu button', 'light gray', 'black'),
    ('bg background', 'default', 'default'),
    ('overheat dark', 'white', 'light red', 'standout'),
    ('bold text', 'default,bold', 'default', 'bold'),
    ('under text', 'default,underline', 'default', 'underline'),

    ('util light', 'default', 'light green'),
    ('util light smooth', 'light green', 'default'),
    ('util dark', 'default', 'dark green'),
    ('util dark smooth', 'dark green', 'default'),

    ('high temp dark', 'default', 'dark red'),
    ('high temp dark smooth', 'dark red', 'default'),
    ('high temp light', 'default', 'light red'),
    ('high temp light smooth', 'light red', 'default'),

    ('power dark', 'default', 'light gray', 'standout'),
    ('power dark smooth', 'light gray', 'default'),
    ('power light', 'default', 'white', 'standout'),
    ('power light smooth', 'white', 'default'),

    ('temp dark', 'default', 'dark cyan', 'standout'),
    ('temp dark smooth', 'dark cyan', 'default'),
    ('temp light', 'default', 'light cyan', 'standout'),
    ('temp light smooth', 'light cyan', 'default'),

    ('freq dark', 'default', 'dark magenta', 'standout'),
    ('freq dark smooth', 'dark magenta', 'default'),
    ('freq light', 'default', 'light magenta', 'standout'),
    ('freq light smooth', 'light magenta', 'default'),

    ('button normal', 'dark green', 'default', 'standout'),
    ('button select', 'white', 'dark green'),
    ('line', 'default', 'default', 'standout'),
    ('pg normal', 'white', 'default', 'standout'),
    ('pg complete', 'white', 'dark magenta'),
    ('high temp txt', 'light red', 'default'),
    ('pg smooth', 'dark magenta', 'default')
]

palette = []

choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()


def minimal_app():
    msg = 'Hello, Songs in One!'
    txt = urwid.Text(('header', msg), align='center')
    fill = urwid.Filler(txt, 'top')
    return fill


def run(widget):
    loop = urwid.MainLoop(widget, unhandled_input=exit_on_q)
    loop.run()


if __name__ == '__main__':
    w = minimal_app()
    run(w)
