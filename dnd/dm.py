# -*- coding: utf-8 -*-
"""
@name:          dm.py
@vers:          0.1.0
@author:        dthor
@created:       Wed Oct 01 15:58:06 2014
@descr:         A new file

Usage:
    dm.py

Options:
    -h --help           # Show this screen.
    --version           # Show version.

Description:
    The DM client of the DnD program. This displays the party's stats,
    including hit points, armor class, etc.

    This is supposed to talk with the PC client over the network.
"""

from __future__ import (print_function, division,
                        absolute_import, unicode_literals)
from docopt import docopt
import Tkinter as tk
import abilities
import char_classes
import char_races
from bottle import route, run, template
try:
    import cPickle as pickle
except:
    import pickle


root = tk.Tk()

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


class MainUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        pass


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


def main():
    """ Main Code """
    docopt(__doc__, version=__version__)
#    root.geometry("1000x700+150+150")
#    app = MainUI(root)
#    root.mainloop()

    run(host='localhost', port=8080)


if __name__ == "__main__":
    main()
