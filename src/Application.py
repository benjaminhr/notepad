from tkinter import *
from tkinter import messagebox
from .File import File
import atexit

# Will contain the states for the application.
class App:

  def __init__(self):
    self.filePath = None

  @property
  def filePath(self):
    return self.__filePath

  @filePath.setter
  def filePath(self, filePath):
    self.__filePath = filePath

class GUI(App):

  def __init__(self, window):
    App.__init__(self)

    window.title("Notepad")
    window.geometry("550x700")
    window.attributes("-topmost", True)
    self.window = window

    self.menu = Menu(self.window)
    self.window.config(menu=self.menu)
    self.__setupMenu(self.menu)

    self.textbox = Text(window)
    GUI.__setupTextbox(self.textbox)

    atexit.register(self.saveBeforeExit)

  def setWindowTitle(self, title):
    self.window.title(title)

  @property
  def text(self):
    # "end-1c" removes extra new line character that a normal end adds 
    return self.textbox.get("1.0", "end-1c")

  @text.setter
  def text(self, text):
    self.textbox.delete('1.0', END)
    self.textbox.insert(INSERT, text or "Type here...")

  def __setupMenu(self, menu):
    file = Menu(menu)
    file.add_command(label = 'Open', command = lambda: File.open(self))
    file.add_command(label = 'Save', command = lambda: File.save(self))
    file.add_command(label = 'Save As', command = lambda: File.saveAs(self))
    file.add_command(label = 'Exit', command = lambda: exit())
    menu.add_cascade(label = 'File', menu = file)

  def __setupTextbox(textbox):
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
  
  def saveBeforeExit(self):
    userWantsToSave = False

    if self.text:
      userWantsToSave = messagebox.askyesno(
        "Unsaved Text", 
        "Do you want to save the text before exiting?"
      )
    
    if userWantsToSave:
      File.save(self)
    else:
      print("Exited without saving")

def start():
  window = Tk()
  GUI(window)
  window.mainloop()
  
 
