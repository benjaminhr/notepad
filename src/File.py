import os
from tkinter import filedialog, Text, BOTH, INSERT, END
from tkinter.filedialog import askopenfilename

class File:
  def updateTextBox(textbox, contents):
    textbox.delete('1.0', END)
    textbox.insert(INSERT, contents or "Type here...")

  def save(window, textbox):
    path = filedialog.asksaveasfilename(
      title = "Select file",
      filetypes = (("Text files","*.txt"), ("all files","*.*"))
    )

    # "end-1c" removes extra new line character that a normal end adds
    contents = textbox.get("1.0", "end-1c")

    """ required as otherwise the following happens:
          - Saves contents to a file with name '()' the first time
          - Throws FileNotFoundError the afterwards time.
    """
    path = ''.join(path)

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
    path = askopenfilename(
      filetypes = (("Text File", "*.txt"), ("All Files","*.*")),
      title = "Choose a file."
    )

    # Required as sometimes it opens up a '()' file if it exists
    path = ''.join(path)

    try:
      with open(path, 'r') as uploadedFile:
        print ("Reading file  " + path)

        head, strippedPath = os.path.split(path)
        window.title(strippedPath)
        contents = uploadedFile.read()
        File.updateTextBox(textbox, contents)

    except FileNotFoundError as e:
      print("Could not open file.")
      print(e)
