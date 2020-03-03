#!/usr/bin/env python3
'''
Passphrase/password generator version 0
'''

from tkinter import *
from tkinter.ttk import *
from PasswordGen import *


class MockWidget(LabelFrame):
    def __init__(self, master=None, context="<description>", **kwargs):
        LabelFrame.__init__(self, master, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.descr = Label(self, text=context)
        self.descr.grid(row=0, column=0, sticky="NEWS")


class App(Frame):
    '''Main window'''

    def __init__(self, master=None, title="Application", **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(title)
        self.grid(sticky="NEWS")

        fAlg = MockWidget(self, text="Algorithm", context="Algorithm menubutton")
        fAlg.grid(row=0, column=0, sticky="NEWS")
        self.rowconfigure(0, weight=0)

        fPar = MockWidget(self, text="Algorithm parameters", context="Algorithm parameters")
        fPar.grid(row=1, column=0, sticky="NEWS")
        self.rowconfigure(1, weight=0)

        fVoc = MockWidget(self, text="Dictionary", context="Dictionary label and menubutton")
        fVoc.grid(row=2, column=0, sticky="NEWS")
        self.rowconfigure(2, weight=0)

        fSep = MockWidget(self, text="Separators", context="Separators label and menubutton")
        fSep.grid(row=3, column=0, sticky="NEWS")
        self.rowconfigure(3, weight=0)

        fPass = MockWidget(self, text="Passwords", context="Passwords multiline label and")
        fPass.grid(row=4, column=0, sticky="NEWS")
        self.rowconfigure(4, weight=1)

        fGen = MockWidget(self, text="Generate", context="Passphrase generation controls")
        fGen.grid(row=5, column=0, sticky="NEWS")
        self.rowconfigure(5, weight=0)

        self.columnconfigure(0, weight=1)


if __name__ == "___main__":
    Prog = App(title="Passphrase generator")
    Prog.mainloop()
