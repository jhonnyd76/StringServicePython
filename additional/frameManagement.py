from tkinter import *


class TextFrames(Frame):
    def __init__(self, master=None, lblText="", lblRow=0, lblColumn=0, entryRow=0, entryColumn=0):
        Frame.__init__(self, master)
        self.label = Label(self, text=lblText, width=30)
        self.label.grid(row=lblRow, column=lblColumn)
        self.text = StringVar()
        self.entry = Entry(self, width=30, textvariable=self.text)
        self.entry.grid(row=entryRow, column=entryColumn)

class LabelEntry():
    def __init__(self, master=None, lblText=""):
        pass