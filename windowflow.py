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

    It handles errors for now.
    Line format:
    #appname|x,y,width,height|delay till app becomes responsive(sec)|arg1|arg2|argn
    '''
    parsed_config = []
    try:
        # check if config file exists 
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Config file {filename} not found.")
        for line in open(filename):
            line = line.strip()
            # if the line is comment or empty, skip it
            if line[0] == '#' or len(line) == 0: 
                continue
            params = line.split('|')
            # check if the line has the correct format
            if len(params) < 4:
                raise ValueError(f"Invalid line format in config file: {line}")
            appname = params[0]
            try:
                x,y, width, height = params[1].split(',')
                x = int(x)
                y = int(y)
                width = int(width)
                height = int(height)                
            except ValueError:
                raise ValueError(f"Invalid line format in config file: {line}")
            try:
                delay = float(params[2])
            except ValueError:
                raise ValueError(f"Invalid delay value in config file: {line}")
            arguments = params[3:]
            parsed_config.append( (appname, (x,y,width,height), delay, arguments ) )
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