# -*- coding: utf-8 -*-
"""
@name:          dice.py
@vers:          0.1.0
@author:        dthor
@created:       Wed Oct 01 15:43:30 2014
@descr:         A new file

Usage:
    dice.py

Options:
    -h --help           # Show this screen.
    --version           # Show version.


What do I want this to do... hmm...

Do I want to simulate rolls? Not really, because
    1   There's already a website to do that
    2   I can do the math easily enough.
            Yay statistics!

I guess it might be useful to find out what the minimum is... nah.

"""

from __future__ import (print_function, division,
                        absolute_import, unicode_literals)
from docopt import docopt

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


class Die(object):
    """ Base class for all die """
    pass


def main():
    """ Main Code """
    docopt(__doc__, version=__version__)


if __name__ == "__main__":
    main()
