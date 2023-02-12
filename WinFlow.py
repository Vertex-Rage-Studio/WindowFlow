from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMainWindow
import sys

class WinFlow:

    path = "./Configs"

    def __init__(self, app):
        self.app = app
        self.initUI()
        

    def initUI(self):
        self.icon = QIcon("Logo.png")

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        self.menu = QMenu()

        self.setup_stored_configs()

        self.menu.addSeparator()

        self.setup_menu_capture()
        self.setup_menu_quit()
        
        self.tray.setContextMenu(self.menu)

    def setup_stored_configs(self):
        self.temp = QAction("TODO: populate with configs")
        self.menu.addAction(self.temp)

    def setup_menu_capture(self):
        self.save = QAction("Capture")
        self.menu.addAction(self.save)

    def setup_menu_quit(self):
        self.quit = QAction("Quit")
        self.quit.triggered.connect(self.app.quit)        
        self.menu.addAction(self.quit)

if __name__ == '__main__':
    app = QApplication([sys.argv])
    app.setQuitOnLastWindowClosed(False)

    winflow = WinFlow(app)
    sys.exit(app.exec_())