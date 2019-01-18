from tkinter import *
from tkinter import messagebox
from .File import File
import atexit

class App:
  def __init__(self, window):    
    self.window = window
    self.textbox = None
  
  def start(self):
    self.window.title("Notepad")
    self.window.geometry("550x700")
    self.window.attributes("-topmost", True)

    self.createMenu()
    self.createTextbox()
    atexit.register(self.saveBeforeExit)    

  def createMenu(self):
    menu = Menu(self.window)
    self.window.config(menu=menu)

    file = Menu(menu)
    file.add_command(label = 'Open', command = lambda: File.open(self.window, self.textbox))
    file.add_command(label = 'Save', command = lambda: File.save(self.window, self.textbox))
    file.add_command(label = 'Exit', command = lambda: exit())
    menu.add_cascade(label = 'File', menu = file)

  def createTextbox(self):
    self.textbox = Text(self.window)
    self.textbox.pack(expand=True, fill=BOTH, pady=(0,7))
    self.textbox.config(
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
  
  def saveBeforeExit(self):
    userWantsToSave = messagebox.askyesno(
      "Unsaved Text", 
      "Do you want to save the text before exiting?"
    )
    
    if userWantsToSave:
      File.save(self.window, self.textbox)
    else:
      print("Exited without saving")

def start():
  window = Tk()
  App(window).start()
  window.mainloop()
  
 