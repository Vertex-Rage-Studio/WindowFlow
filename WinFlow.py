from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import subprocess

path = "./Configs"
dir_list = os.listdir(path)

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Adding an icon
icon = QIcon("Logo.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options
menu = QMenu()
option2 = QAction("Save")

for i in dir_list:
    count = 1
    string = str(count)
    (string) = QAction(i)
    menu.addAction(i)
    count += 1

menu.addSeparator()
menu.addAction(option2)

# Runs Load Script
file = QAction()
file.triggered.connect(
    subprocess.run('python windowflow.py -c' + file.text())
)
# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

menu.setStyleSheet(
    "background-color: rgb(20, 20, 20);"
    "border: 1px solid rgb(40, 40, 40);"
    "color: rgb(150, 150, 150);"
)
# Adding options to the System Tray
tray.setContextMenu(menu)

app.exec_()