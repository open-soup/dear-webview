import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import parsehtml as parser
import PySide6.QtGui as QtGui
from PySide6.QtGui import QFont
import threading
import itertools

def render():
 app = QtWidgets.QApplication([]) 
 window = QtWidgets.QWidget()
 window.resize(800, 600)
 window.setWindowTitle("Dear Webiew")
 layout = QtWidgets.QVBoxLayout(window)
 layout.setSpacing(5) 
 layout.setContentsMargins(5, 1, 5, 1)
 
 rendercontent = parser.getcontent("example.html")
 print(rendercontent)
 for item in rendercontent:
    if item.endswith("A2SDLPOJ"):
        item = item.replace("A2SDLPOJ", "")
        font_size = 15
    elif item.endswith("A1SDLPOJ"):
        item = item.replace("A1SDLPOJ", "")
        font_size = 10
    else:
        font_size = 25



    label = QtWidgets.QLabel(item)
    font = QtGui.QFont()
    font.setPointSize(font_size)
    label.setFont(font)
    label.setAlignment(QtCore.Qt.AlignLeft)
    layout.addWidget(label)
    label.setWordWrap(False)     # no wrapping
    label.setFixedHeight(font_size + 10)  # consistent height padding
 icon = QtGui.QIcon("DWDB.png")
 window.setWindowIcon(icon)
 


 window.show()  
 sys.exit(app.exec())
