# here the main applciation will live
# mainly for imported a class, etc and using it once

import tkinter

def start():
  window = tkinter.Tk()
  window.title("Notepad")

  # window size
  window.geometry("500x500")

  # forces window to front
  window.attributes("-topmost", True)
  
  # pack() puts the widget in the GUI window
  label = tkinter.Label(window, text = "Hello Karmjit!").pack()

  # keeps window open
  window.mainloop()
