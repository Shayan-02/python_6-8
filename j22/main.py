from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.browser.urlChanged.connect(self.update_urlbar)

        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navigation = QToolBar("Navigation")
        self.addToolBar(navigation)

        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navigation.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navigation.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navigation.addAction("home_btn")

        navigation.addSeparator()

        self.urlbar = QLineEdit()

        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navigation.addAction(stop_btn)

        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Haj Alex" % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")
        self.browser.setUrl(q)

    def update_urlbar(self):
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("Haj Alex")
window = MainWindow()
app.exec()