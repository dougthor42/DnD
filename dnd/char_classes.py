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


class CharClass(object):
    # This is needed so that TestType is an Abstract Base Class
    # PY3: changes when porting to Python3
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass


class Barbarian(CharClass):
    def __init__(self):
        pass


class Bard(CharClass):
    def __init__(self):
        pass


class Cleric(CharClass):
    def __init__(self):
        pass


class Druid(CharClass):
    def __init__(self):
        pass


class Fighter(CharClass):
    def __init__(self):
        pass


class Monk(CharClass):
    def __init__(self):
        pass


class Paladin(CharClass):
    def __init__(self):
        pass


class Ranger(CharClass):
    def __init__(self):
        pass


class Sorcorer(CharClass):
    def __init__(self):
        pass


class Warlock(CharClass):
    def __init__(self):
        pass


class Wizard(CharClass):
    def __init__(self):
        pass


def main():
    """ Main Code """
    pass

if __name__ == "__main__":
    main()
