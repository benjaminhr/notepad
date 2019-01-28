from tkinter import *

class FileMenu:
  def __init__(self, window):
    fileMenu = Frame(window, bg="red", width=220)
    fileMenu.columnconfigure(0)
    fileMenu.grid(row=0, column=0, sticky=N+S+W)