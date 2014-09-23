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
import Tkinter

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


class Example(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")

        self.pack(fill=Tkinter.BOTH, expand=1)

        quitButton = Tkinter.Button(self, text="Quit",
                                    command=self.buttonClick)
        quitButton.place(x=50, y=50)
        
        self.var = Tkinter.IntVar()
        check_button = Tkinter.Checkbutton(self, text='hellp',
                                           variable=self.var,
                                           command=self.onClick)

        check_button.select()
        check_button.place(x=15, y=15)

        classes = ['A',
                   'B',
                   'C',
                   ]

        list_box = Tkinter.Listbox(self)
        for _i in classes:
            list_box.insert(Tkinter.END, _i)

        list_box.bind("<<ListboxSelect>>", self.onSelect)
        list_box.place(x=120, y=50)

        self.string_var = Tkinter.StringVar()
        self.label = Tkinter.Label(self, text=0, textvariable=self.string_var)
        self.label.place(x=120, y=210)

        self.spin_var = 0
        spinbox = Tkinter.Spinbox(self,
                                  values=range(31),
                                  command=self.onSpinChange,
                                  )
        self.spinbox = spinbox
        spinbox.pack()
        spinbox.place(x=300, y=50)

        self.str_var = Tkinter.IntVar()
        textbox = Tkinter.Entry(self, textvariable=self.str_var)
        textbox.pack()
        textbox.place(x=300, y=100)

    def onClick(self):
        if self.var.get() == 1:
            self.master.title("Checkbutton")
            self.str_var.set(self.str_var.get() + 1)
        else:
            self.master.title("")

    def buttonClick(self):
        print("clicked!")

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.string_var.set(value)

    def onSpinChange(self):
        self.str_var.set("{}".format((int(self.spinbox.get()) // 2) - 5))


def main():
    """ Main Code """
    docopt(__doc__, version=__version__)
    root = Tkinter.Tk()
    root.geometry("450x350+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == "__main__":
    main()
