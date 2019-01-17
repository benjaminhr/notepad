# here the main applciation will live
# mainly for imported a class, etc and using it once

from tkinter import Tk, Frame, Button, Text, INSERT, LEFT, X, BOTH
from .File import File

def start():
  window = Tk()
  window.title("Notepad")

  # window size
  window.geometry("500x500")

  # forces window to front
  window.attributes("-topmost", True)

  # padx and pady set x and y padding
  toolbar = Frame(window)
  toolbar.pack(fill=X, padx=7, pady=7)

  openFileBtn = Button(toolbar, text="Open File", command=File.open)
  openFileBtn.pack(side=LEFT)

  # padding is added to space out buttons
  saveFileBtn = Button(toolbar, text="Save File", command=File.save)
  saveFileBtn.pack(side=LEFT, padx=5)

  textBox = Text(window)
  # pady is (0,7) as there are there are 7px of spcaing on the toolbar
  textBox.pack(expand=True, fill=BOTH, padx=7, pady=(0,7))

  textBox.insert(INSERT,"Hello there...\nHow are you Benjamin?")

  # keeps window open
  window.mainloop()
