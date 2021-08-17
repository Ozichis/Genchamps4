import sys
from PyQt5.Qt import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

web = QWebEngineView()

web.load(QUrl("https://google.com"))

web.show()

sys.exit(app.exec_())