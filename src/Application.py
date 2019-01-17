# here the main applciation will live
# mainly for imported a class, etc and using it once

from tkinter import Tk, Frame, Button, INSERT, LEFT, X, BOTH, Menu
from .File import File

def start():
  window = Tk()
  window.title("Notepad")

  # window size
  window.geometry("500x500")

  # forces window to front
  window.attributes("-topmost", True)

  menu = Menu(window)
  window.config(menu=menu)

  file = Menu(menu)
  file.add_command(label = 'Open', command = File.open)
  file.add_command(label = 'Save', command = File.save)
  file.add_command(label = 'Exit', command = lambda:exit())
  menu.add_cascade(label = 'File', menu = file)

  window.mainloop()

  # padx and pady set x and y padding
  # toolbar = Frame(window)
  # toolbar.pack(fill=X, padx=7, pady=7)

  # create textbox with file contents and name

  # openFileBtn = Button(toolbar, text="Open File", command=File.open)
  # openFileBtn.pack(side=LEFT)

  # padding is added to space out buttons
  # saveFileBtn = Button(toolbar, text="Save File", command=File.save)
  # saveFileBtn.pack(side=LEFT, padx=5)

  
  # keeps window open