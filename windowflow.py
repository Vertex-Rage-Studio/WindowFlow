import sys
import os
import subprocess
import win32gui
import win32api
import win32con
import time


def get_set_of_window_titles(hwnd, output):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        output.add(title)
    
def main():
    #config_file = sys.argv[1]

    app_name = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    app_params = 'https://google.com'

    start_windows = set([])

    win32gui.EnumWindows(get_set_of_window_titles, start_windows)

    print(start_windows)

    print("Launching...", app_name)

    subprocess.Popen([app_name, app_params])
    time.sleep(0.5) # that's stupid, but it works for now
    active = win32gui.GetForegroundWindow()
    print(win32gui.GetWindowText(active))
    win32gui.SetWindowPos(active, None, 10, 10, 1000, 500, win32con.SWP_SHOWWINDOW)


if __name__ == "__main__":
    main()