# here the main applciation will live
# mainly for imported a class, etc and using it once

from tkinter import *
from .File import File

def start():
  window = Tk()
  window.title("Notepad")
  window.geometry("550x700")
  # forces window to front
  window.attributes("-topmost", True)

  menu = Menu(window)
  window.config(menu=menu)

  textbox = Text(window)
  textbox.pack(expand=True, fill=BOTH, pady=(0,7))
  textbox.config(
    padx = 25,
    pady = 25, 
    borderwidth = 0,
    font = "{Courier} 16",
    foreground = "white",
    background = "black",
    insertbackground = "white", # cursor
    selectforeground = "grey", # selection
    selectbackground = "#008000",
    wrap = WORD, # use word wrapping
    width = 64,
    undo = True,
  )

  file = Menu(menu)
  file.add_command(label = 'Open', command = lambda: File.open(textbox))
  file.add_command(label = 'Save', command = lambda: File.save(textbox))
  file.add_command(label = 'Exit', command = lambda: exit())
  menu.add_cascade(label = 'File', menu = file)

  # keeps window open
  window.mainloop()

  
