from termcolor import colored
import random

def show():
    banner_art = """
   _____                  ______                               
  / ___/____  ____ ______/ ____/___  ____ ___  ____  ____  ____ 
  \__ \/ __ \/ __ `/ ___/ /   / __ \/ __ `__ \/ __ \/ __ \/ __ \\
 ___/ / /_/ / /_/ (__  ) /___/ /_/ / / / / / / /_/ / /_/ / /_/ /
/____/ .___/\__,_/____/\____/\____/_/ /_/ /_/ .___/\____/\____/ 
    /_/                                    /_/                  

        📸 SpyCam Hunter – Find Open Cams Like a Ghost
    """

    colors = ['cyan', 'green', 'magenta', 'yellow']
    banner_colored = colored(banner_art, random.choice(colors), attrs=['bold'])
    print(banner_colored)

    print(colored(" [+] Coded by: HansdaTechs", "Shibnath Hansda"))
    print(colored(" [+] Purpose : Ethical Network Camera Recon Tool", "white"))
    print(colored(" [+] Warning : For Educational Use Only ⚠️", "red"))
    print()
  
