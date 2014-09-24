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
import Tkinter as tk
import abilities

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")

        self.stat_block = StatBlockFrame(self)
        self.stat_block.place(x=10, y=10)

        self.pack(fill=tk.BOTH, expand=1)

#        close_button = tk.Button(self, text='Close')
#        close_button.pack(side=tk.RIGHT, padx=5, pady=5)
#        ok_button = tk.Button(self, text='OK')
#        ok_button.pack(side=tk.RIGHT)
#
#        self.quitButton = tk.Button(self,
#                                    text="Quit",
#                                    command=self.buttonClick,
#                                    )
#        self.quitButton.place(x=500, y=300)
#
#        self.var = tk.IntVar()
#        self.check_button = tk.Checkbutton(self, text='hellp',
#                                           variable=self.var,
#                                           command=self.onClick,
#                                           )
#
#        self.check_button.select()
#        self.check_button.place(x=300, y=300)

#        classes = ['A',
#                   'B',
#                   'C',
#                   ]
#
#        list_box = tk.Listbox(self)
#        for _i in classes:
#            list_box.insert(tk.END, _i)
#
#        list_box.bind("<<ListboxSelect>>", self.onSelect)
#        list_box.place(x=250, y=50)
#
#        self.string_var = tk.StringVar()
#        self.label = tk.Label(self, text=0, textvariable=self.string_var)
#        self.label.place(x=120, y=210)

    def onClick(self):
        if self.var.get() == 1:
            self.master.title("Checkbutton")
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


class AbilityScoreFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.points = 0
        self.score_base = -5
        self.score = self.score_base

        self.proficient_var = tk.IntVar()
        self.proficient_var.set(0)

        self.score_var = tk.IntVar()
        self.score_var.set(self.score)

        self.pack(fill=tk.BOTH, expand=1)

        self.vcmd = (self.parent.register(self.spin_validate),
                     '%P')
        self.points_spinbox = tk.Spinbox(self,
                                         values=range(31),
                                         command=self.on_spin_change,
                                         validate='focusout',
                                         validatecommand=self.vcmd,
                                         )

        self.points_spinbox.pack()
        self.points_spinbox.place(x=0, y=0, width=30)

        self.score_textbox = tk.Entry(self, textvariable=self.score_var)
        self.score_textbox.pack()
        self.score_textbox.place(x=35, y=0, width=30)

        self.proficient_checkbox = tk.Checkbutton(self,
                                                  variable=self.proficient_var,
                                                  command=self.on_proficiency_change,
                                                  )
        self.proficient_checkbox.pack()
        self.proficient_checkbox.place(x=70, y=0)



    def on_spin_change(self):
        self.spin_validate(int(self.points_spinbox.get()))
        return 1

    def spin_validate(self, P):
        self.points = int(P)
        self.score_base = (self.points // 2) - 5
        if self.proficient_var.get() == 1:
            self.score = self.score_base + 2
        else:
            self.score = self.score_base
        self.score_var.set("{}".format(self.score))
        return 1

    def on_proficiency_change(self):
        if self.proficient_var.get() == 1:
            self.score = self.score_base + 2
        else:
            self.score = self.score_base
        self.score_var.set("{}".format(self.score))


class SkillFrame(tk.Frame):
    def __init__(self, parent, skill_name="skill"):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.skill_name = skill_name
        self.init_ui()

    def init_ui(self):
        self.points = 0
        self.score_base = 0
        self.score = self.score_base

        self.proficient_var = tk.IntVar()
        self.proficient_var.set(0)

        self.score_var = tk.IntVar()
        self.score_var.set(self.score)

        self.label = tk.Label(self,
                              text=self.skill_name,
                              anchor='e',
                              width=15
                              )
        self.label.grid(row=0, column=0)

        self.proficient_checkbox = tk.Checkbutton(self,
                                                  variable=self.proficient_var,
                                                  command=self.on_proficiency_change,
                                                  )
        self.proficient_checkbox.grid(row=0, column=1)

        self.score_textbox = tk.Entry(self,
                                      textvariable=self.score_var,
                                      width=2,
                                      justify='center')
        self.score_textbox.grid(row=0, column=2)

    def on_proficiency_change(self):
        if self.proficient_var.get() == 1:
            self.score = self.score_base + 2
        else:
            self.score = self.score_base
        self.score_var.set("{}".format(self.score))


class SkillFrameBlock(tk.Frame):
    def __init__(self, parent, ability):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.ability = ability
        self.init_ui()

    def init_ui(self):
        if len(abilities.SKILLS[self.ability]) == 0:
#            tk.Label(self,
#                     text="-",
#                     justify='center',
#                     width=15,
#                     ).grid(row=0, column=0)
            SkillFrame(self, '').grid(row=0, column=0)
        else:
            for _i, _a in enumerate(abilities.SKILLS[self.ability]):
                SkillFrame(self, _a).grid(row=_i, column=0)


class AbilityBlock(tk.Frame):
    def __init__(self, parent, ability):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.ability = ability
        self.init_ui()

    def init_ui(self):
        self.points = 0
        self.score_base = -5
        self.score = self.score_base

        self.proficient_var = tk.IntVar()
        self.proficient_var.set(0)

        self.score_var = tk.IntVar()
        self.score_var.set(self.score)

        self.saving_throw = 0
        self.saving_throw_value = tk.IntVar()
        self.saving_throw_value.set(self.saving_throw)

#        self.pack(fill=tk.BOTH, expand=1)

        self.vcmd = (self.parent.register(self.spin_validate),
                     '%P')
        self.points_spinbox = tk.Spinbox(self,
                                         values=range(31),
                                         command=self.on_spin_change,
                                         validate='focusout',
                                         validatecommand=self.vcmd,
                                         width=4,
                                         justify='center',
                                         )

#        self.points_spinbox.pack()
#        self.points_spinbox.place(x=0, y=0, width=30)
        self.points_spinbox.grid(row=0, column=0)

        self.score_textbox = tk.Entry(self,
                                      textvariable=self.score_var,
                                      width=4,
                                      justify='center',
                                      )
#        self.score_textbox.pack()
#        self.score_textbox.place(x=35, y=0, width=30)
        self.score_textbox.grid(row=0, column=1)

        self.proficient_checkbox = tk.Checkbutton(self,
                                                  variable=self.proficient_var,
                                                  command=self.on_proficiency_change,
                                                  )
#        self.proficient_checkbox.pack()
#        self.proficient_checkbox.place(x=70, y=0)
        self.proficient_checkbox.grid(row=0, column=2)

        self.saving_throw_display = tk.Entry(self,
                                     textvariable=self.saving_throw_value,
                                     width=4,
                                     justify='center',
                                     )

        self.saving_throw_display.grid(row=0, column=3)

        self.skill_block = SkillFrameBlock(self, self.ability)
        self.skill_block.grid(row=0, column=4)

    def on_spin_change(self):
        self.spin_validate(int(self.points_spinbox.get()))
        return 1

    def spin_validate(self, P):
        self.points = int(P)
        self.score_base = (self.points // 2) - 5
        if self.proficient_var.get() == 1:
            self.saving_throw = self.score_base + 2
        else:
            self.saving_throw = self.score_base
        self.score_var.set("{}".format(self.score_base))
        self.saving_throw_value.set("{}".format(self.saving_throw))
        return 1

    def on_proficiency_change(self):
        if self.proficient_var.get() == 1:
            self.saving_throw = self.score_base + 2
        else:
            self.saving_throw = self.score_base
        self.saving_throw_value.set("{}".format(self.saving_throw))


class StatBlockFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        for _i, stat in enumerate(abilities.SKILLS.keys()):
            AbilityBlock(self, stat).grid(row=_i, column=0)

def main():
    """ Main Code """
    docopt(__doc__, version=__version__)
    root = tk.Tk()
    root.geometry("1000x700+150+150")
    app = Example(root)
    root.mainloop()


if __name__ == "__main__":
    main()
