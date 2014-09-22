# -*- coding: utf-8 -*-
"""
@name:          new_program.py
@vers:          0.1.0
@author:        dthor
@created:       Mon Sep 22 16:28:15 2014
@descr:         A new file

Usage:
    new_program.py

Options:
    -h --help           # Show this screen.
    --version           # Show version.
"""

from __future__ import (print_function, division,
                        absolute_import, unicode_literals)
from docopt import docopt
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",
                            command=self.quit)
        quitButton.place(x=50, y=50)


def main():
    """ Main Code """
    docopt(__doc__, version=__version__)
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == "__main__":
    main()
