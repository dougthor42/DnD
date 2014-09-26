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
import char_classes
import char_races
try:
    import cPickle as pickle
except:
    import pickle

__author__ = "Douglas Thor"
__version__ = "v0.1.0"

root = tk.Tk()


class UIVars(object):
    """ Contains all the UI Variables """
    def __init__(self):
        self.proficiency_bonus = tk.IntVar()
        self.proficiency_bonus.set(2)

        self.ability_points = {}
        self.ability_score = {}
        self.ability_proficient = {}
        self.ability_saving_throw = {}

        self.skill_proficient = {}
        self.skill_score = {}
        self.skill_score_display = {}

        for stat in abilities.ABILITIES:
            self.ability_points[stat] = tk.IntVar()
            self.ability_points[stat].set(0)

            self.ability_score[stat] = tk.IntVar()
            self.ability_score[stat].set(-5)

            self.ability_proficient[stat] = tk.IntVar()
            self.ability_proficient[stat].set(0)

            self.ability_saving_throw[stat] = tk.IntVar()
            self.ability_saving_throw[stat].set(0)

            for skill in abilities.SKILLS[stat]:
                self.skill_proficient[skill] = tk.IntVar()
                self.skill_proficient[skill].set(0)

                self.skill_score[skill] = tk.IntVar()
                self.skill_score[skill].set(-5)

                self.skill_score_display[skill] = tk.IntVar()
                self.skill_score_display[skill].set(-5)


global ui_vars
ui_vars = UIVars()


class UIVarValues(object):
    """ Contains all of the UI Variables' values (only) """
    def __init__(self):
        self.proficiency_bonus = ui_vars.proficiency_bonus.get()

        self.ability_points = {}
        self.ability_score = {}
        self.ability_proficient = {}
        self.ability_saving_throw = {}

        self.skill_proficient = {}
        self.skill_score = {}
        self.skill_score_display = {}

        for stat in abilities.ABILITIES:
            self.ability_points[stat] = ui_vars.ability_points[stat].get()
            self.ability_score[stat] = ui_vars.ability_score[stat].get()
            self.ability_proficient[stat] = ui_vars.ability_proficient[stat].get()
            self.ability_saving_throw[stat] = ui_vars.ability_saving_throw[stat].get()

            for skill in abilities.SKILLS[stat]:
                self.skill_proficient[skill] = ui_vars.skill_proficient[skill].get()
                self.skill_score[skill] = ui_vars.skill_score[skill].get()
                self.skill_score_display[skill] = ui_vars.skill_score_display[skill].get()


def strip_ui_var_values():
    """ Strips the values from each Tkinter variable in the UIVars class """
    return UIVarValues()


def load_ui_var_values(values):
    """ Loads values into each Tkinter variable in the UIVars class """
    ui_vars.proficiency_bonus.set(values.proficiency_bonus)

    for stat in abilities.ABILITIES:
        ui_vars.ability_points[stat].set(values.ability_points[stat])
        ui_vars.ability_score[stat].set(values.ability_score[stat])
        ui_vars.ability_proficient[stat].set(values.ability_proficient[stat])
        ui_vars.ability_saving_throw[stat].set(values.ability_saving_throw[stat])

        for skill in abilities.SKILLS[stat]:
            ui_vars.skill_proficient[skill].set(values.skill_proficient[skill])
            ui_vars.skill_score[skill].set(values.skill_score[skill])
            ui_vars.skill_score_display[skill].set(values.skill_score_display[skill])


class MainUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")

#        labels = ['Ability','Points','Score','Proficient','Saving Throw']

        list_box = tk.Listbox(self)
        for _i in char_races.RACES:
            list_box.insert(tk.END, _i)

        list_box.bind("<<ListboxSelect>>", self.onSelect)
        list_box.place(x=10, y=10)

        list_box = tk.Listbox(self)
        for _i in char_classes.CLASSES:
            list_box.insert(tk.END, _i)

        list_box.bind("<<ListboxSelect>>", self.onSelect)
        list_box.place(x=10, y=200)

        self.stat_block = StatBlockFrame(self)
        self.stat_block.place(x=150, y=10)

        save_button = tk.Button(self,
                                text='Save',
                                command=self.save_click,
                                )
        save_button.place(x=10, y=400)

        load_button = tk.Button(self,
                                text='Load',
                                command=self.load_click,
                                )
        load_button.place(x=60, y=400)

        self.pack(fill=tk.BOTH, expand=1)

#        self.var = tk.IntVar()
#        self.check_button = tk.Checkbutton(self, text='hellp',
#                                           variable=self.var,
#                                           command=self.onClick,
#                                           )
#
#        self.check_button.select()
#        self.check_button.place(x=300, y=300)

#        self.string_var = tk.StringVar()
#        self.label = tk.Label(self, text=0, textvariable=self.string_var)
#        self.label.place(x=120, y=210)

    def save_click(self):
        """ Saves the UI Variables to a file. """
        # I can't pickle Tkinter variables (IntVar, etc.) directly, so I
        # created a function to strip the value from them. I then pickle
        # this value.
        print("Saving data!")
        ui_values = strip_ui_var_values()
#        with open("X:\\WinPython27\\projects\\github\\DnD\\trunk\\dnd\\pickle.txt", 'w') as of:
        with open("pickle.txt", 'w') as of:
            pickle.dump(ui_values, of)

    def load_click(self):
        """ Load the UI Variablres from a file. """
        # Since I can't pickle Tkinter variables directly, the file only
        # contains the value of the variables. I have to read the values and
        # then recreate and set each variable.
        print("Loading Data!")
        with open("pickle.txt", 'r') as of:
            ui_values = pickle.load(of)
            load_ui_var_values(ui_values)

#    def onClick(self):
#        if self.var.get() == 1:
#            self.master.title("Checkbutton")
#        else:
#            self.master.title("")

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        print(value)

#        self.string_var.set(value)

    def onSpinChange(self):
        self.str_var.set("{}".format((int(self.spinbox.get()) // 2) - 5))


class SkillFrame(tk.Frame):
    def __init__(self, parent, skill="skill"):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.skill = skill
        self.init_ui()

    def init_ui(self):
        self.score = ui_vars.skill_score[self.skill]

        self.proficient_var = ui_vars.skill_proficient[self.skill]

        self.displayed_score_var = ui_vars.skill_score_display[self.skill]
#        self.temp_score_var = ui_vars.skill_score[self.skill]
#        self.score_var.set(self.score)

        self.label = tk.Label(self,
                              text=self.skill,
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
                                      textvariable=self.displayed_score_var,
                                      width=2,
                                      justify='center')
        self.score_textbox.grid(row=0, column=2)

    def on_proficiency_change(self):
        if self.proficient_var.get() == 1:
            temp_score = self.score.get() + ui_vars.proficiency_bonus.get()
        else:
            temp_score = self.score.get()
        self.displayed_score_var.set("{}".format(temp_score))


class SkillFrameEmpty(tk.Frame):
    def __init__(self, parent, skill=''):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.skill = skill
        self.init_ui()

    def init_ui(self):
        self.label = tk.Label(self,
                              text=self.skill,
                              anchor='e',
                              width=15
                              )
        self.label.grid(row=0, column=0)

        self.proficient_checkbox = tk.Checkbutton(self)
        self.proficient_checkbox.grid(row=0, column=1)

        self.score_textbox = tk.Entry(self,
                                      width=2,
                                      justify='center')
        self.score_textbox.grid(row=0, column=2)


class AbilityBlock(tk.Frame):
    def __init__(self, parent, ability):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.ability = ability
        self.init_ui()

    def init_ui(self):
        # declare instance attributes
        self.points = 0
        self.score_base = -5
        self.score = self.score_base

        self.proficient_var = ui_vars.ability_proficient[self.ability]
        self.proficient_var.set(0)

        self.score_var = ui_vars.ability_score[self.ability]
        self.score_var.set(self.score)

        self.saving_throw = 0
        self.saving_throw_value = ui_vars.ability_saving_throw[self.ability]
        self.saving_throw_value.set(self.saving_throw)

        self.skill_count = len(abilities.SKILLS[self.ability])
        if self.skill_count == 0:
            self.skill_count = 1

        self.label = tk.Label(self,
                              text=self.ability,
                              width=10,
                              )
        self.label.grid(row=0,
                        column=0,
                        rowspan=self.skill_count,
                        )

        # create a ValidateCommand for the spinbox so that it updates
        # the related scores when a user types in a value (rather than
        # just updaing on an arrow click)
        self.vcmd = (self.parent.register(self.ability_point_change),
                     '%P')
        self.points_spinbox = tk.Spinbox(self,
                                         values=range(31),
                                         textvariable=ui_vars.ability_points[self.ability],
                                         command=self.on_spin_change,
                                         validate='focusout',
                                         validatecommand=self.vcmd,
                                         width=4,
                                         justify='center',
                                         )
        self.points_spinbox.grid(row=0,
                                 column=1,
                                 rowspan=self.skill_count,
                                 )

        self.score_textbox = tk.Entry(self,
                                      textvariable=self.score_var,
                                      width=4,
                                      justify='center',
                                      )
        self.score_textbox.grid(row=0,
                                column=2,
                                rowspan=self.skill_count,
                                )

        self.proficient_checkbox = tk.Checkbutton(self,
                                                  variable=self.proficient_var,
                                                  command=self.on_proficiency_change,
                                                  )
        self.proficient_checkbox.grid(row=0,
                                      column=3,
                                      rowspan=self.skill_count,
                                      )

        self.saving_throw_display = tk.Entry(self,
                                             textvariable=self.saving_throw_value,
                                             width=4,
                                             justify='center',
                                             )

        self.saving_throw_display.grid(row=0,
                                       column=4,
                                       rowspan=self.skill_count,
                                       )

        # New method of adding the skill block - allows the other stuff to
        # span the columns
        if len(abilities.SKILLS[self.ability]) == 0:
            SkillFrameEmpty(self).grid(row=0, column=5)
        else:
            for _i, _a in enumerate(abilities.SKILLS[self.ability]):
                SkillFrame(self, _a).grid(row=_i, column=5)

    def on_spin_change(self):
        self.ability_point_change(int(self.points_spinbox.get()))
        return 1

    def ability_point_change(self, P):
        self.points = int(P)
        self.score_base = (self.points // 2) - 5
        if self.proficient_var.get() == 1:
            self.saving_throw = self.score_base + 2
        else:
            self.saving_throw = self.score_base
        self.score_var.set("{}".format(self.score_base))
        self.saving_throw_value.set("{}".format(self.saving_throw))
        for skill in abilities.SKILLS[self.ability]:
            ui_vars.skill_score[skill].set("{}".format(self.score_base))
            if ui_vars.skill_proficient[skill].get() == 1:
                ui_vars.skill_score_display[skill].set("{}".format(self.score_base + ui_vars.proficiency_bonus.get()))
            else:
                ui_vars.skill_score_display[skill].set("{}".format(self.score_base))
        return 1

    def on_proficiency_change(self):
        if self.proficient_var.get() == 1:
            self.saving_throw = self.score_base + 2
        else:
            self.saving_throw = self.score_base
        self.saving_throw_value.set("{}".format(self.saving_throw))


# Obsolete
class StatBlockFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief=tk.GROOVE, borderwidth=1)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        for _i, stat in enumerate(abilities.ABILITIES):
            AbilityBlock(self, stat).grid(row=_i, column=0)

def main():
    """ Main Code """
    docopt(__doc__, version=__version__)
#    root = tk.Tk()
    root.geometry("1000x700+150+150")
    app = MainUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
