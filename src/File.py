import os
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class File:
  def save(app, path=None):
    if path is None and app.filePath is None:
      path = asksaveasfilename(title = "Select file")
      path = ''.join(path)
      app.filePath = path
    elif path is None:
      path = app.filePath

    contents = app.text

    try:
      with open(path, 'w') as toSaveAsFile:
        print("Saving text to path " + path)
        head, strippedPath = os.path.split(path)
        app.setWindowTitle(strippedPath)
        toSaveAsFile.write(contents);

    except FileNotFoundError as e:
        print("Could not save text to file")
        print(e)

  def saveAs(app):
      path = asksaveasfilename(title = "Select file")
      path = ''.join(path)

      if not path is None:
        app.filePath = path
        File.save(app, path)
      

  def open(app):
    path = askopenfilename(title = "Choose a file.")
    path = ''.join(path)

    app.filePath = path 

    try:
      with open(path, 'r') as uploadedFile:
        contents = uploadedFile.read()
        app.text = contents
        print ("Reading file  " + path)

        head, strippedPath = os.path.split(path)
        app.setWindowTitle(strippedPath)

    except FileNotFoundError as e0:
      print("Error", "Could not open file.",e0)
    except Exception as e1:
      print("ERROR","Unpredicted Error")
      print(e1, file=sys.stderr)
