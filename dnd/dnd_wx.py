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

from __future__ import print_function, division, absolute_import
#from __future__ import unicode_literals
from docopt import docopt
import wx
from pubsub import pub
import abilities
import char_classes
import char_races
try:
    import cPickle as pickle
except:
    import pickle

__author__ = "Douglas Thor"
__version__ = "v0.1.0"

BORDER = wx.NO_BORDER
#BORDER = wx.SIMPLE_BORDER


class SkillPanelEmpty(wx.Panel):
    """
    The SkillPanelEmpty panel. Special case for CON where no skills are
    associated with it.
    """
    def __init__(self, parent, skill="None"):
        wx.Panel.__init__(self, parent, style=BORDER)
        self.skill = skill
        self.message_lbl = "updating_text_{}".format(self.skill)
        self.init_ui()

    def init_ui(self):
        # Add layout management
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.fgs = wx.FlexGridSizer(1, 3, 0, 5)

        # Create the items that we'll add
        self.label = wx.StaticText(self,
                                   label=self.skill,
                                   style=wx.ALIGN_RIGHT,
                                   size=(80, -1)
                                   )

        self.proficient = wx.CheckBox(self,
                                      style=wx.ALIGN_RIGHT,
                                      )

#        self.proficient.Bind(wx.EVT_CHECKBOX, self.send_update)

        self.skill_val = wx.StaticText(self,
                                       label="0",
                                       style=wx.ALIGN_CENTER,
                                       size=(20, -1)
                                       )

        # Add items to our layout manager
        self.fgs.AddMany([self.label,
                          self.proficient,
                          self.skill_val,
                          ])
        self.hbox.Add(self.fgs)

        # Set the sizer
        self.SetSizer(self.hbox)


class SkillPanel(wx.Panel):
    """
    The SkillFrame panel. Contains the skill name (Athletics, Insight, etc.),
    a proficiency checkbox, and a score value.

    This is (currently) the lowest-level item.
    """
    def __init__(self, parent, skill="None"):
        wx.Panel.__init__(self, parent, style=BORDER)
        self.skill = skill
        self.message_lbl = "updating_text_{}".format(self.skill)
        self.init_ui()

    def init_ui(self):
        # Add layout management
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.fgs = wx.FlexGridSizer(1, 3, 0, 5)

        # Create the widgets that we'll add
        self.label = wx.StaticText(self,
                                   label=self.skill,
                                   style=wx.ALIGN_RIGHT,
                                   size=(80, -1)
                                   )

        self.proficient = wx.CheckBox(self,
                                      style=wx.ALIGN_RIGHT,
                                      )

        self.skill_val = wx.StaticText(self,
                                       label="0",
                                       style=wx.ALIGN_CENTER,
                                       size=(20, -1)
                                       )

        # Bind any events
        self.proficient.Bind(wx.EVT_CHECKBOX, self.send_update)

        # Add items to our layout manager
        self.fgs.AddMany([self.label,
                          self.proficient,
                          self.skill_val,
                          ])
        self.hbox.Add(self.fgs)

        # Set the sizer
        self.SetSizer(self.hbox)
        
        # Register listeners
        pub.subscribe(self.update_text, self.message_lbl)

    # Create listener
    def update_text(self, value):
        """ Update the label text when a message is received """
        val = int(self.skill_val.GetLabel())
        if value == 1:
            val += 2
        else:
            val -= 2
        self.skill_val.SetLabel(str(val))

    def send_update(self, event):
        print(event.GetInt())
        pub.sendMessage(self.message_lbl, value=event.GetInt())


class SkillBlock(wx.Panel):
    """
    A SkillBlock panel. Contains all the skills associated with a
    given ability. Handles the logic for when the ability has no skills
    associated with it (the CON case).
    """
    def __init__(self, parent, ability="None"):
        wx.Panel.__init__(self, parent, style=wx.SIMPLE_BORDER)
        self.ability = ability
        self.skill_count = len(abilities.SKILLS[self.ability])
        if self.skill_count == 0:
            self.skill_count == 1
        self.init_ui()

    def init_ui(self):
        # Add layout management
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.fgs = wx.FlexGridSizer(rows=self.skill_count, cols=1, 
                                    vgap=2, hgap=2)

        # Create the widgets that we'll add
        if self.ability == "Constitution":
            self.fgs.Add(SkillPanel(self, ""),
                         )
        else:
            for n, skill in enumerate(abilities.SKILLS[self.ability]):
                self.fgs.Add(SkillPanel(self, skill),
                             )

        # Add items to our layout manager and set the sizer
        self.hbox.Add(self.fgs)
        self.SetSizer(self.hbox)


class AbilitySubBlock(wx.Panel):
    """
    Contains the centered items for ability block.
        ability
        points
        pase score
        prodiciecy
        actual score
    """
    def __init__(self, parent, ability="None"):
        wx.Panel.__init__(self, parent, style=BORDER)
        self.ability = ability
        self.init_ui()

    def init_ui(self):
        # Add layout management
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        # generate the widgets
        self.label = wx.StaticText(self,
#                                   wx.ID_ANY,
                                   size=(120, -1),
                                   label=self.ability,
                                   style=wx.ALIGN_CENTER,
                                   )

        self.points = wx.SpinCtrl(self,
                                  wx.ID_ANY,
                                  size=(40, -1),
                                  style=wx.ALIGN_CENTER,
                                  )

        # Add widgets to the layout manager
        self.hbox.Add(self.label, flag=wx.ALIGN_CENTER_VERTICAL)
        self.hbox.Add(self.points, flag=wx.ALIGN_CENTER_VERTICAL)

        # Set the sizer
        self.SetSizer(self.hbox)



class AbilityBlock(wx.Panel):
    """
    AbilityBlock panel which contains:
        ability
        points
        base score
        proficiency
        actual score
        array of associated skills
    """
    def __init__(self, parent, ability="None"):
        wx.Panel.__init__(self, parent, style=wx.SIMPLE_BORDER)
        self.ability = ability
        self.init_ui()

    def init_ui(self):
        # Add layout management
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.fgs = wx.FlexGridSizer(rows=1, cols=2, vgap=2, hgap=2)

        # Add items to the layout manager
        self.fgs.Add(AbilitySubBlock(self, self.ability),
#                     flag=wx.EXPAND,
                     flag=wx.ALIGN_CENTER_VERTICAL,
                     )

        self.fgs.Add(SkillBlock(self, self.ability),
                     flag=wx.ALIGN_CENTER_VERTICAL,
                     )

        self.hbox.Add(self.fgs, flag=wx.ALL, border=3)

        # Set the sizer
        self.SetSizer(self.hbox)


class Abilities(wx.Panel):
    """
    Abilities panel which contains multiple AbilityBlocks
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.init_ui()

    def init_ui(self):
        # Add layout management
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.gbs = wx.GridBagSizer()
    
        # Add items
        col_titles = ("Ability",
                      "Proficient",
                      "Score",
                      "Modifier",
                      "Save",
                      "Skills"
                      )
        for _n, text in enumerate(col_titles):
            self.gbs.Add(wx.StaticText(self,
                                       label=text,
                                       style=wx.ALIGN_CENTER,
                                       ),
                         pos=(0, _n),
                         )
    
    
        for _n, ability in enumerate(abilities.ABILITIES):
            self.gbs.Add(AbilityBlock(self, ability),
                         pos=(_n + 1, 0),
                         )

        # Set the sizer
        self.hbox.Add(self.gbs)
        self.SetSizer(self.hbox)


class MainPanel(wx.Panel):
    """
    This is the main panel of the application. It contains all other panels.
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.init_ui()
#        self.parent = parent

    def init_ui(self):
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        
        self.race_choice = wx.Choice(self,
                                     choices=[_i for _i in char_races.RACES],
#                                     style=wx.CB_READONLY,
                                     )
        self.race_choice.SetSelection(0)
        self.race_choice.Bind(wx.EVT_CHOICE, self.race_change)
#
#        self.combo_box.Bind(wx.EVT_COMBOBOX, self.send_update)
#
#        self.text = wx.StaticText(self,
#                                  wx.ID_ANY,
#                                  pos=(50, 50),
#                                  label="Hello",
#                                  )
#
#        # register listener
#        pub.subscribe(self.update_text, 'updating text')

        self.hbox.Add(self.race_choice)
        self.hbox.Add(Abilities(self))
        self.SetSizer(self.hbox)

    def race_change(self, event):
        print(event.GetInt())

#    # create listener
#    def update_text(self, value):
#        """ Update the label text when a message is received """
#        self.text.SetLabel(value)
#
#    def send_update(self, event):
#        print(event.GetString())
#        print(event.GetInt())
#        pub.sendMessage('updating text', value=event.GetString())


class MainWindow(wx.Frame):
    """
    This is the main window of the application. It contains the MainPanel
    and the MenuBar.

    Although technically I don't need to have only 1 panel in the MainWindow,
    I can have multiple panels. But I think I'll stick with this for now.
    """
    def __init__(self, title, size=(800, 600)):
        wx.Frame.__init__(self,
                          None,
                          wx.ID_ANY,
                          title=title,
                          size=size,
                          )
#        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.panel = MainPanel(self)
        self.Show(True)


def main():
    """ Main Code """
    print("Running...")
    docopt(__doc__, version=__version__)
    # Create a new app, don't redirect stdout/stderr to a window.
    app = wx.App(False)
    # A Frame is a top-level window.
    frame = MainWindow("Test")
    # Show the frame.
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
