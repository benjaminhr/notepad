# here the main applciation will live
# mainly for imported a class, etc and using it once

from tkinter import Tk, filedialog, Frame, Button, Text, INSERT, LEFT, X, BOTH

def openFile():
  # opens a panel asking the user to select a file
  # NOTICE: It can throw an exception if you close the panel
  file = filedialog.askopenfilename(title = "Select file")
  print("Opening file " + file)

def saveFile():
  # opens a "save as" panel
  # NOTICE: It can throw an exception if you close the panel
  fileToSaveAs = filedialog.asksaveasfilename(title = "Select file",filetypes = (("Text files","*.txt"),("all files","*.*")))
  print("Saving text to file " + fileToSaveAs)

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

  openFileBtn = Button(toolbar, text="Open File", command=openFile)
  openFileBtn.pack(side=LEFT)

  # padding is added to space out buttons
  saveFileBtn = Button(toolbar, text="Save File", command=saveFile)
  saveFileBtn.pack(side=LEFT, padx=5)

  textBox = Text(window)
  # pady is (0,7) as there are there are 7px of spcaing on the toolbar
  textBox.pack(expand=True, fill=BOTH, padx=7, pady=(0,7))

  textBox.insert(INSERT,"Hello there...\nHow are you Benjamin?")

  # keeps window open
  window.mainloop()
