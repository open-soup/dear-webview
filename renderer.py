import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
import parsehtml as parser
import PySide6.QtGui as QtGui
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
import hashlib
import requests

def render():
    app = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    window.resize(800, 600)
    window.setWindowTitle("Dear Webiew")
    layout = QtWidgets.QVBoxLayout(window)
    layout.setSpacing(5)
    layout.setContentsMargins(5, 1, 5, 1)

    # Set window icon once
    icon = QtGui.QIcon("DWDB.png")
    window.setWindowIcon(icon)

    rendercontent = parser.getcontent("example.html")
    print(rendercontent)

    for item in rendercontent:
        font_size = 10  # default

        if item.endswith("A2SDLPOJ"):
            item = item.replace("A2SDLPOJ", "")
            font_size = 15
            is_text = True
        elif item.endswith("A1SDLPOJ"):
            item = item.replace("A1SDLPOJ", "")
            font_size = 10
            is_text = True
        elif item.endswith("COPL█J"):
            item = item.replace("COPL█J", "")
            font_size = 5
            is_text = True
        elif item.endswith("/ħŧŧptimg-Đone"):
            url = item.replace("/ħŧŧptimg-Đone", "").strip()
            url_hash = hashlib.md5(url.encode()).hexdigest()
            r = requests.get(url)
            with open(f"{url_hash}.jpg", "wb") as f:
                f.write(r.content)
            pixmap = QPixmap(f"{url_hash}.jpg")
            label = QLabel()
            label.setPixmap(pixmap)
            layout.addWidget(label)
            continue

        else:
            is_text = True
            font_size = 15

        if is_text:
            label = QLabel(item)
            font = QtGui.QFont()
            font.setPointSize(font_size)
            label.setFont(font)
            label.setAlignment(QtCore.Qt.AlignLeft)
            layout.addWidget(label)
            label.setWordWrap(False)
            label.setFixedHeight(font_size + 10)

    window.show()
    sys.exit(app.exec())