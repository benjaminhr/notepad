from tkinter import filedialog

class File:
  def save():
    # NOTICE: It can throw an exception if you close the panel
    fileToSaveAs = filedialog.asksaveasfilename(
      title = "Select file",
      filetypes = (("Text files","*.txt"), ("all files","*.*"))
    )
    
    print("Saving text to file " + fileToSaveAs)
  
  def open():
    # NOTICE: It can throw an exception if you close the panel
    file = filedialog.askopenfilename(title = "Select file")
    print("Opening file " + file)