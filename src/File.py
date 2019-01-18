from tkinter import filedialog, Text, BOTH, INSERT, END
from tkinter.filedialog import askopenfilename

class File:
  def updateTextBox(textbox, contents):
    textbox.delete('1.0', END)
    textbox.insert(INSERT, contents or "Type here...")

  def save(textbox):
    name = filedialog.asksaveasfilename(
      title = "Select file",
      filetypes = (("Text files","*.txt"), ("all files","*.*"))
    )

    # "end-1c" removes extra new line character that a normal end adds
    contents = textbox.get("1.0", "end-1c")

    """ required as otherwise the following happens:
          - Saves contents to a file with name '()' the first time
          - Throws FileNotFoundError the afterwards time.
    """
    name = ''.join(name)

    try:
      with open(name, 'w') as toSaveAsFile:
        print("Saving text to file " + name)
        toSaveAsFile.write(contents);
        print("Text:\n" + contents)
    except FileNotFoundError as e:
        print("Could not save text to file")
        print(e)

  def open(textbox):
    name = askopenfilename(
      filetypes = (("Text File", "*.txt"), ("All Files","*.*")),
      title = "Choose a file."
    )

    # Required as sometimes it opens up a '()' file if it exists
    name = ''.join(name)

    try:
      with open(name, 'r') as uploadedFile:
        print ("Reading file  " + name)
        contents = uploadedFile.read()
        File.updateTextBox(textbox, contents)
        print("Text:\n" + contents)
    except FileNotFoundError as e:
      # can also be thrown when the panel asking for a file is closed directly
      print("Could not open file.")
      print(e)
