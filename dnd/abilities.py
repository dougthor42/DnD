# -*- coding: utf-8 -*-
"""
@name:          new_program.py
@vers:          0.1.0
@author:        dthor
@created:       Tue Sep 23 14:30:13 2014
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
from enum import Enum       # Py3: Not needed >= 3.4

__author__ = "Douglas Thor"
__version__ = "v0.1.0"

# List the abilities, in the order we want displayed
ABILITIES = ("Strength", "Dexterity", "Constitution",
             "Intelligence", "Wisdom", "Charisma")

# Dict of the skills that correspond to each ability
SKILLS = {"Strength": ("Athletics", ),
          "Dexterity": ("Acrobatics", "Slight of Hand", "Stealth"),
          "Constitution": (),
          "Intelligence": ("Arcana", "History", "Investigation",
                           "Nature", "Religion"),
          "Wisdom": ("Animal Handling", "Insight", "Medicine",
                     "Perception", "Survival"),
          "Charisma": ("Deception", "Intimidation",
                       "Performance", "Persuasion"),
          }


class Ability(object):
    # This is needed so that TestType is an Abstract Base Class
    # PY3: changes when porting to Python3
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractproperty
    def skills(self):
        pass


class Strength(Ability):
    skills = SKILLS["Strength"]

    def __init__(self):
        pass


class Dexterity(Ability):
    skills = SKILLS["Dexterity"]

    def __init__(self):
        pass


class Constitution(Ability):
    skills = SKILLS["Constitution"]

    def __init__(self):
        pass


class Intelligence(Ability):
    skills = SKILLS["Intelligence"]

    def __init__(self):
        pass


class Wisdom(Ability):
    skills = SKILLS["Wisdom"]

    def __init__(self):
        pass


class Charisma(Ability):
    skills = SKILLS["Charisma"]

    def __init__(self):
        pass


def main():
    """ Main Code """
    print(Strength.skills)

if __name__ == "__main__":
    main()
