import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction

class App(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("LOLPad")
    self.setGeometry(0, 0, 640, 480)
   
    mainMenu = self.menuBar()
    self.__genFileMenu(mainMenu)

    self.show()

  def __genFileMenu(self, mainMenu):
    fileMenu = mainMenu.addMenu('File')
    newFileButton = QAction('New File', self)
    newFileButton.setShortcut('Ctrl+N')
    fileMenu.addAction(newFileButton)

    openFileButton = QAction('Open', self)
    openFileButton.setShortcut('Ctrl+O')
    fileMenu.addAction(openFileButton)

    saveFileButton = QAction('Save', self)
    saveFileButton.setShortcut('Ctrl+S')
    fileMenu.addAction(saveFileButton)

    saveAsFileButton = QAction('Save As', self)
    saveAsFileButton.setShortcut('Ctrl+Shift+S')
    fileMenu.addAction(saveAsFileButton)

    exitButton = QAction('Exit', self)
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit application')
    exitButton.triggered.connect(self.close)
    fileMenu.addAction(exitButton)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  ex = App()
  sys.exit(app.exec_())
