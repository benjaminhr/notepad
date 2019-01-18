from tkinter import filedialog, Text, BOTH, INSERT, END
from tkinter.filedialog import askopenfilename

class File:
  def updateTextBox(textbox, contents):
    textbox.delete('1.0', END)
    textbox.insert(INSERT, contents or "Type here...")

  def save(textbox):
    # NOTICE: It can throw an exception if you close the panel
    try:
      name = filedialog.asksaveasfilename(
        title = "Select file",
        filetypes = (("Text files","*.txt"), ("all files","*.*"))
      )

      print("Saving text to file " + name)

      # "end-1c" removes extra new line character that a normal end adds
      contents = textbox.get("1.0", "end-1c")
      print("Text:\n" + contents)

      with open(name, 'w') as toSaveAsFile:
        toSaveAsFile.write(contents);
    except Exception as e:
      print(e)
  

  def open(textbox):
    name = askopenfilename(
      filetypes = (("Text File", "*.txt"), ("All Files","*.*")),
      title = "Choose a file."
    )
    print ("file name: " + name)
    
    # try if unknown file or closes without choosing a file
    try:
      with open(name, 'r') as uploadedFile:
        contents = uploadedFile.read()
        File.updateTextBox(textbox, contents)
    except Exception as e: 
      print(e)
