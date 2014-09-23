# -*- coding: utf-8 -*-
"""
@name:          new_program.py
@vers:          0.1.0
@author:        dthor
@created:       Tue Sep 23 13:21:18 2014
@descr:         A new file

Usage:
    new_program.py

Options:
    -h --help           # Show this screen.
    --version           # Show version.
"""

from __future__ import (print_function, division,
                        absolute_import, unicode_literals)
import abc

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


class Race(object):
    # This is needed so that TestType is an Abstract Base Class
    # PY3: changes when porting to Python3
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass


class Dwarf(Race):
    def __init__(self):
        pass


class Elf(Race):
    def __init__(self):
        pass


class Halfling(Race):
    def __init__(self):
        pass


class Human(Race):
    def __init__(self):
        pass


class Dragonborn(Race):
    def __init__(self):
        pass


class HalfElf(Race):
    def __init__(self):
        pass


class HalfOrc(Race):
    def __init__(self):
        pass


class Gnome(Race):
    def __init__(self):
        pass


class Tiefling(Race):
    def __init__(self):
        pass



def main():
    """ Main Code """
    pass

if __name__ == "__main__":
    main()
