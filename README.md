![alt text](https://github.com/Vertex-Rage-Studio/WindowFlow/raw/main/Static/Logo.svg)

<br>

# WindowFlow
*Effortlessly restore and organize your workspace with our customizable app launcher.*

I often have multiple projects running simultaneously and it always frustrated me that I couldn't easily restore my workspace. By workspace, I mean a set of windows that are opened and positioned appropriately. For example, one workspace may consist of Firefox with three tabs maximized on one screen, two file explorers side by side on the other screen, and Unreal Engine on top of it.

Inspired by Curtis Holt's recent video (https://www.youtube.com/watch?v=SDawvvcx1dE), I began searching for a solution to this problem. However, it seemed that there were none available for Windows or they were quite expensive for such a simple functionality. After discussing with Mathew in Curtis's Discord community, we decided to create our own solution.

Here it is - the first version, which has relatively simple functionality. It launches all the apps based on a manually written config file and places them in set positions. More updates will come in the future (hopefully).

It needs python and depends on pywin32 (https://pypi.org/project/pywin32/) for it's functionality. 

To run the example confing file you simply type:

python windowflow.py config_test.cfg

The example config file will run: 
- explorer.exe pointint at C:\Users at location (100, 100) and size of window of (900,700)
- it will open 2 new tabs in firefox, one pointing to google, one to bing (or if it's not launched - should launch a new window and open those 2 tabs)
- it will run another explorer.exe (without path) at (500,300) and size of window of (900, 700)
- it will launch new firefox window, open blender.org site and move it to the 2nd screen on the left (example config assumes that you have one)
- it will launch Blender with D:\tmp\test.blend, and move it to (0,0) and set it's size to (2500,1380)
- it will launch pureref with D:\AssetsLibrary\Ref\low-poly-graveyard.pur on the second screen and will make it's window take almost full screen

Of course you will not have the .blend and .pur file or you might not have even firefox installed, so adjust the config to your needs.

# Roadmap

- ~~step 1: - make it launch apps based on manually written config file~~ Done
- step 2: tool for helping in writing the config file
- step 3: UX
