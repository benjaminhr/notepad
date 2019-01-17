from tkinter import filedialog, Text
from tkinter.filedialog import askopenfilename

class File:
  def updateTextBox(contents):
    textBox = Text(window)
    # pady is (0,7) as there are there are 7px of spcaing on the toolbar
    textBox.pack(expand=True, fill=BOTH, padx=7, pady=(0,7))
    textBox.insert(INSERT, contents | "Type here...")

  def save():
    # NOTICE: It can throw an exception if you close the panel
    fileToSaveAs = filedialog.asksaveasfilename(
      title = "Select file",
      filetypes = (("Text files","*.txt"), ("all files","*.*"))
    )
    
    print("Saving text to file " + fileToSaveAs)
  
  def open(window):
    name = askopenfilename(
      filetypes = (("Text File", "*.txt"), ("All Files","*.*")),
      title = "Choose a file."
    )
    print ("file name: " + name)
    
    # try if unknown file or closes without choosing a file
    try:
      with open(name, 'r') as uploadedFile:
        contents = uploadedFile.read()
        File.updateTextBox(contents)
        print(contents)
    except Exception as e: 
      print(e)
