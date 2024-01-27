import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon 
 
class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.browser = QWebEngineView()
        
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    background-color: yellow;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to Simple Browser</h1>
            <p>This is a custom background example.</p>
        </body>
        </html>
        """
 
        self.browser.setHtml(html_content)
        
        self.browser.setUrl(QUrl("http://www.google.com"))
 
        self.setCentralWidget(self.browser)
 
        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)
 
        # Back button
        back_btn = QAction('Back', self)
        back_btn.setStatusTip('Back to previous page')
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
 
        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.setStatusTip('Forward to next page')
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
 
        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.setStatusTip('Reload page')
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
 
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
 
        # Home button
        home_btn = QAction('Home', self)
        home_btn.setStatusTip('Go home')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
 
        # Stop button
        stop_btn = QAction('Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)
 
        # Setting up the main window
        self.showMaximized()
 
        # Set window icon
        self.setWindowIcon(QIcon('icon.png'))
 
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))
 
    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
 
        self.browser.setUrl(q)
 
app = QApplication(sys.argv)
QApplication.setApplicationName("PoochBrowser")
window = SimpleBrowser()
app.exec_()
