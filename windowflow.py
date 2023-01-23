import sys
import os
import argparse
import subprocess
import win32gui
import win32api
import win32con
import time

from subprocess import CREATE_NEW_CONSOLE

def parse_config(filename):
    '''
    Parses the config file.

    chatgpt was used to handle error handling and simplification of this function

    Line format:
    #appname|x,y,width,height|delay till app becomes responsive(sec)|arg1|arg2|argn
    '''
    parsed_config = []
    try:
        # check if config file exists 
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Config file {filename} not found.")
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                appname, window_position, delay, shell, *arguments = line.split("|")
                x, y, width, height = map(int, window_position.split(","))
                delay = float(delay)
                shell = bool(shell)
                parsed_config.append((appname, (x, y, width, height), delay, shell, arguments))
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    return parsed_config



def get_set_of_window_titles(hwnd, output):
    '''
    Not used yet, gets all windows titles
    '''
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        output.add(title)

def restore_session(config_parsed):
    '''
    Restores windows layout based on current config file
    '''
    for c in config_parsed:
        app_name, (x, y, w, h), delay, shell, args = c
        
        params = [app_name, *args]
        subprocess.Popen(params, creationflags=CREATE_NEW_CONSOLE if shell else 0)

        time.sleep(delay) # that's stupid, but it works for now

        if x == y == w == h == 0: # for 0,0,0,0 don't set size, just launch the app
            continue
        
        active = win32gui.GetForegroundWindow()
        win32gui.SetWindowPos(active, None, x,y,w,h, win32con.SWP_SHOWWINDOW)

def write_config(config_file):
    '''
    With help of chatgpt - not working fully yet (no paths to exe, no delays and shell params), 
    but putting it up for future reference.
    '''
    try:
        with open(config_file, "w", encoding='utf-8') as f:
            f.write("#appname|x,y,width,height|arg1|arg2|argn\n")
            def enum_cb(hwnd, windows):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    # check if the title is empty
                    if title:
                        rect = win32gui.GetWindowRect(hwnd)
                        x, y, width, height = rect
                        windows.append((title, (x, y, width, height)))
            windows = []
            win32gui.EnumWindows(enum_cb, windows)
            for title, (x, y, width, height) in windows:
                f.write(f"{title}|{x},{y},{width},{height}|\n")
    except Exception as e:
        print("Error:", e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", default="restore-session", choices=["store-session", "restore-session"], help="Mode")
    parser.add_argument("-c", "--config", required=True, help="Path to config file")
    args = parser.parse_args()

    config_file = args.config

    if args.mode == "store-session":
        print("Not yet implemented")
    else:
        config_parsed = parse_config(config_file)
        restore_session(config_parsed)


    # start_windows = set([])
    # win32gui.EnumWindows(get_set_of_window_titles, start_windows)
    # print(start_windows)

if __name__ == "__main__":
    main()