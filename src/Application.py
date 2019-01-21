from tkinter import *
from tkinter import messagebox
from .File import File
from random import randint
import atexit
import subprocess

class App(Frame): 
  def __init__(self, window=None):
    Frame.__init__(self, window)

    self.filePath = None
    self.grid(sticky=N+S+E+W)
    self.window = self.winfo_toplevel()
    self.window.title("Notepad")
    self.window.geometry("550x700+%d+%d" % (randint(100, 400), randint(100, 300)))
    self.window.protocol("WM_DELETE_WINDOW", exit)

    self.menu = Menu(self.window, bd=0)
    self.window['menu'] = self.menu
    self.textbox = Text(self)
    self.__setupMenu()
    self.__setupTextbox()
    self.__setupLayout()

    atexit.register(self.saveBeforeExit)

  def __setupLayout(self):
    self.window.columnconfigure(0, weight=1)
    self.window.rowconfigure(0, weight=1)

    self.columnconfigure(0,weight=1)
    self.rowconfigure(0, weight=1)

    self.textbox.columnconfigure(0, weight=1)
    self.textbox.rowconfigure(0, weight=1)

  def __setupMenu(self):
    file = Menu(self.menu, tearoff=0, bd=0, activeborderwidth=0)
    file.add_command(label = 'New File', command = lambda: subprocess.Popen(["python3", "start.py"]))
    file.add_command(label = 'Open', command = lambda: File.open(self))
    file.add_command(label = 'Save', command = lambda: File.save(self))
    file.add_command(label = 'Save As', command = lambda: File.saveAs(self))
    file.add_command(label = 'Exit', command = lambda: exit())
    self.menu.add_cascade(label = 'File', menu = file)

  def __setupTextbox(self):
    self.textbox.grid(row=0, column=0, sticky=N+E+S+W)
    self.textbox.config(
      padx = 10,
      pady = 10,
      borderwidth = 0,
      highlightthickness = 0,
      font = "{Courier} 16",
      foreground = "white",
      background = "black",
      insertbackground = "white", 
      selectforeground = "grey",
      selectbackground = "#008000",
      wrap = WORD,
      width = 64,
      undo = True
    )

  def setWindowTitle(self, title):
    self.window.title(title)

  @property
  def text(self):
    # "end-1c" removes extra new line character that a normal end adds 
    return self.textbox.get("1.0", "end-1c")

  @text.setter
  def text(self, text):
    self.textbox.delete('1.0', END)
    self.textbox.insert(INSERT, str(text) or "Type here...")

  @property
  def textModified(self):
    return self.textbox.edit_modified()

  @textModified.setter
  def textModified(self, flag):
    self.textbox.edit_modified(flag)

  def saveBeforeExit(self):
    if self.textModified and (self.filePath or self.text) :
      userWantsToSave = messagebox.askyesno(
        "Unsaved Text", 
        "Do you want to save the text before exiting?"
      )
      if userWantsToSave:
        File.save(self)
      else:
        print("Exited without saving")


def start():
  app = App()
  app.mainloop()