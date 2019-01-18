import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class File:
  def updateTextBox(textbox, contents):
    textbox.delete('1.0', END)
    textbox.insert(INSERT, contents or "Type here...")

  def save(window, textbox):
    path = asksaveasfilename(title = "Select file")
    path = ''.join(path)
    # "end-1c" removes extra new line character that a normal end adds
    contents = textbox.get("1.0", "end-1c")

    try:
      with open(path, 'w') as toSaveAsFile:
        print("Saving text to path " + path)
        head, strippedPath = os.path.split(path)
        window.title(strippedPath)
        toSaveAsFile.write(contents);

    except FileNotFoundError as e:
        print("Could not save text to file")
        print(e)

  def open(window, textbox):
    path = askopenfilename(title = "Choose a file.")
    path = ''.join(path)   

    try:
      with open(path, 'r') as uploadedFile:
        contents = uploadedFile.read()
        File.updateTextBox(textbox, contents)
        head, strippedPath = os.path.split(path)
        window.title(strippedPath)
        
        print ("Reading file  " + path)

    except Exception as e:
      messagebox.showerror("Error", "Could not open file.")
      print(e)
