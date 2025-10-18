import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import parsehtml as parser
import PySide6.QtGui as QtGui



app = QtWidgets.QApplication([])


def render():
 window = QtWidgets.QWidget()
 window.resize(800, 600)
 window.setWindowTitle("Dear Webiew")
 layout = QtWidgets.QVBoxLayout(window)
 rendercontent = parser.getcontent("example.html")
 layout.setSpacing(1) 
 for item in rendercontent:
    label = QtWidgets.QLabel(item)
    layout.addWidget(label)
    label.setAlignment(QtCore.Qt.AlignLeft)


 icon = QtGui.QIcon("DWDB.png")
 window.setWindowIcon(icon)


 window.show()  
 sys.exit(app.exec())
