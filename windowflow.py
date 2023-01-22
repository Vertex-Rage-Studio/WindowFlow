import sys
import os
import subprocess
import win32gui
import win32api
import win32con
import time

def parse_config(filename):
    '''
    Not handling any errors for now.
    Line format:
    #appname|x,y,width,height|arguments|delay till app becomes responsive(sec)
    '''

    parsed_config = []
    for line in open(filename):
        print(line)
        line = line.strip()
        if line[0] == '#' or len(line) == 0: 
            continue
        params = line.split('|')

        appname = params[0]
        x,y, width, height = params[1].split(',')
        arguments = params[2]
        delay = float(params[3])

        parsed_config.append( (appname, (x,y,width,height), arguments, delay ) )

    return parsed_config

def get_set_of_window_titles(hwnd, output):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        output.add(title)
    
def main():
    #config_file = sys.argv[1]
    config_file = 'config_test.cfg'

    app_name = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    app_params = '-new-window https://google.com'

    start_windows = set([])

    win32gui.EnumWindows(get_set_of_window_titles, start_windows)

    print(start_windows)

    print("Launching...", app_name)

    subprocess.Popen([app_name, app_params])
    time.sleep(0.5) # that's stupid, but it works for now
    active = win32gui.GetForegroundWindow()
    print(win32gui.GetWindowText(active))
    win32gui.SetWindowPos(active, None, -1920, 0, 1000, 1030, win32con.SWP_SHOWWINDOW)

    config_parsed = parse_config(config_file)
    for c in config_parsed:
        app_name = c[0]
        position = c[1]
        args = c[2]
        delay = c[3]
        print(app_name, position, args, delay)


if __name__ == "__main__":
    main()