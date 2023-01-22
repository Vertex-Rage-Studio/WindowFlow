import sys
import os
import subprocess
import win32gui
import win32api
import win32con
import time

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
                appname, window_position, delay, *arguments = line.split("|")
                x, y, width, height = map(int, window_position.split(","))
                delay = float(delay)
                parsed_config.append((appname, (x, y, width, height), delay, arguments))
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
        app_name = c[0]
        x,y,w,h = c[1]
        delay = c[2]
        args = c[3]
        
        params = [app_name]
        params.extend(args)

        subprocess.Popen(params)
        time.sleep(delay) # that's stupid, but it works for now
        active = win32gui.GetForegroundWindow()
        win32gui.SetWindowPos(active, None, x,y,w,h, win32con.SWP_SHOWWINDOW)
    
def main():
    config_file = sys.argv[1]

    # start_windows = set([])
    # win32gui.EnumWindows(get_set_of_window_titles, start_windows)
    # print(start_windows)

    config_parsed = parse_config(config_file)

    restore_session(config_parsed)




if __name__ == "__main__":
    main()