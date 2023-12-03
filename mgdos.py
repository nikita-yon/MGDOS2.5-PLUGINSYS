from ast import Try
import time
from colorama import Fore, Back
from colorama import Style
from colorama import init as colorama_init
import os
import sys
import wmi
import atexit
import configparser
from time import sleep 
from itertools import cycle 
import datetime as dt
from datetime import datetime, timedelta
from alive_progress import alive_bar
from time import sleep
from itertools import cycle
from time import sleep
from PIL import Image
from subprocess import call
from playsound import playsound
import webbrowser
import keyboard as keyb
import operator
import psutil
import random
import platform
import re
import curses
from datetime import datetime
from deep_translator import GoogleTranslator
import shutil
from datetime import datetime, timedelta
from time import sleep 
from itertools import cycle
import sys
import msvcrt
import subprocess
import winsound
import threading
from ast import Try
import time
from colorama import Fore, Back
from colorama import Style
from colorama import init as colorama_init
import os
import sys
import wmi
import atexit
import configparser
from time import sleep 
from itertools import cycle 
import datetime as dt
from datetime import datetime, timedelta
from alive_progress import alive_bar
from time import sleep
from itertools import cycle
from time import sleep
from PIL import Image
from subprocess import call
from playsound import playsound
import webbrowser
import keyboard as keyb
import operator
import psutil
import random
import platform
import re
import curses
from datetime import datetime
from deep_translator import GoogleTranslator
import shutil
from datetime import datetime, timedelta
from time import sleep 
from itertools import cycle
import sys
import msvcrt
import subprocess
import winsound
import threading
import itertools
import time 
from pytimedinput import timedInput
from random import randint
import os
from colorama import Fore, init
from importlib import import_module
#from plugin_files import PLUGIN_FILES
import random
import pyaudio
import struct
import math


#executable_directory = os.path.dirname(os.path.abspath(__file__))
#plugins_folder = os.path.join(executable_directory, "Plugins")
#plugin_files = [file[:-3] for file in os.listdir(plugins_folder) if file.endswith(".py")]
#loaded_plugins = plugin_files
#from loaded_plugins import LOADED_PLUGINS, REGISTERED_FUNCTIONS

#import_module("Plugins." + loaded_plugins)

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()


def data_for_freq(frequency: float, time: float = None):
    """get frames for a fixed frequency for a specified time or
    number of frames, if frame_count is specified, the specified
    time is ignored"""
    frame_count = int(RATE * time)

    remainder_frames = frame_count % RATE
    wavedata = []

    for i in range(frame_count):
        a = RATE / frequency  # number of frames per wave
        b = i / a
        

        c = b * (2 * math.pi)
        # explanation for c
        # now we map b to between 0 and 2*math.PI
        # since 0 - 2*PI, 2*PI - 4*PI, ...
        # are the repeating domains of the sin wave (so the decimal values will
        # also be mapped accordingly,
        # and the integral values will be multiplied
        # by 2*PI and since sin(n*2*PI) is zero where n is an integer)
        d = math.sin(c) * 32767
        e = int(d)
        wavedata.append(e)

    for i in range(remainder_frames):
        wavedata.append(0)

    number_of_bytes = str(len(wavedata))  
    wavedata = struct.pack(number_of_bytes + 'h', *wavedata)

    return wavedata


def play(frequency: float, time: float):
    """
    play a frequency for a fixed time!
    """
    frames = data_for_freq(frequency, time)
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    stream.write(frames)
    stream.stop_stream()
    stream.close()

MGDOSVER = "2.5 "  # Ваша версия MG-DOS

clear = lambda: os.system("cls")





def onecheck():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=4):
            break
        print("Checking activation key... ", i,end='\r') 
        sleep(0.3)

def one():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=2):
            break
        print("Collecting data about CFG-FILES... ", i,end='\r') 
        sleep(0.1)

def two():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=2):
            break
        print("Loading command information and saved data... ", i,end='\r') 
        sleep(0.2)

def tre():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("Updating resourses from Github... ", i,end='\r') 
        sleep(0.2)

def chet():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=2):
            break
        print("Cheking screen resolution... ", i,end='\r') 
        sleep(0.1)

def pat():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("calculating... ", i,end='\r') 
        sleep(0.1)

def shest():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=4):
            break
        print("Downloading resourses... ", i,end='\r') 
        sleep(0.4)

def sem():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("calculating... ", i,end='\r') 
        sleep(0.2)

def translate():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("translating... ", i,end='\r') 
        sleep(0.2)

def enc():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("encrypting... ", i,end='\r') 
        sleep(0.2)
def dec():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("decrypting... ", i,end='\r') 
        sleep(0.2)


def vom():
    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print("collecting system information... ", i,end='\r') 
        sleep(0.2)

def format_size(size_in_bytes):
    # Function to format size from bytes to a human-readable format
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            break
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} {unit}"

def format_size(size_in_bytes):
    # Функция для форматирования размера из байтов в человеко-читаемый формат
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            break
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.1f} {unit}"

def list_directory(path="."):
    # Функция для вывода содержимого директории в формате, аналогичном выводу команды "dir" в Windows
    print("{:<19} {:<15} {:<12} {:>20} {}".format("Date", "Time", "Type", "Size", "FileName").upper())
    print(" " * 80)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        item_stat = os.stat(item_path)
        mod_time = dt.datetime.fromtimestamp(item_stat.st_mtime)
        if os.path.isdir(item_path):
            type_str = "<DIR>"
            size_str = ""
        else:
            type_str = ""
            size_str = format_size(item_stat.st_size)
        print("{:<19} {:<15} {:<12} {:>20} {}".format(
            mod_time.strftime("%d.%m.%Y"),
            mod_time.strftime("%H:%M"),
            type_str,
            size_str,
            item
        ))

    total_size = sum(os.stat(os.path.join(path, item)).st_size for item in os.listdir(path) if os.path.isfile(os.path.join(path, item)))
    print(" " * 80)
    print("{:>31} files {:>36}".format(len(os.listdir(path)), format_size(total_size)))

def run(file_path):
    
        subprocess.run(file_path, shell=True)


def YorN():
    key = msvcrt.getch().decode("utf-8")
    if key == "y":
        pass




def text_in_box(content):
    container_width = 12
    container_height = 8

    lines = content.strip().split("\n")
    lines = [line.ljust(container_width - 2) for line in lines]
    container = ["╔" + "═" * (container_width - 2) + "╗"]
    container.extend(["║" + line + "║" for line in lines[:container_height - 2]])
    container.extend(["║" + " " * (container_width - 2) + "║"] * (container_height - 2 - len(lines)))
    container.append("╚" + "═" * (container_width - 2) + "╝")

    for line in container:
        print(line)
def KBSTART():
    
    print("0001")
    time.sleep(0.1)
    clear = lambda: os.system("cls")
    clear()
    print("00001 KB OK")
    time.sleep(0.1)
    clear()
    print("00002 KB OK")
    time.sleep(0.1)
    clear()
    print("00004 KB OK")
    time.sleep(0.1)
    clear()
    print("00011 KB OK")
    time.sleep(0.1)
    clear()
    print("00014 KB OK")
    time.sleep(0.1)
    clear()
    print("00019 KB OK")
    time.sleep(0.1)
    clear()
    print("00020 KB OK")
    time.sleep(0.1)
    clear()
    print("00021 KB OK")
    time.sleep(0.1)
    clear()
    print("00023 KB OK")
    time.sleep(0.1)
    clear()
    print("00025 KB OK")
    time.sleep(0.05)
    clear()
    print("00027 KB OK")
    time.sleep(0.05)
    clear()
    print("00029 KB OK")
    time.sleep(0.05)
    clear()
    print("00030 KB OK")
    time.sleep(0.05)
    clear()
    print("00039 KB OK")
    time.sleep(0.05)
    clear()
    print("00059 KB OK")
    time.sleep(0.05)
    clear()
    print("00062 KB OK")
    time.sleep(0.05)
    clear()
    print("00065 KB OK")
    time.sleep(0.05)
    clear()
    print("00080 KB OK")
    time.sleep(0.05)
    clear()
    print("00089 KB OK")
    time.sleep(0.05)
    clear()
    print("00092 KB OK")
    time.sleep(0.05)
    clear()
    print("00102 KB OK")
    time.sleep(0.05)
    clear()
    print("00112 KB OK")
    time.sleep(0.05)
    clear()
    print("00129 KB OK")
    time.sleep(0.05)
    clear()
    print("00131 KB OK")
    time.sleep(0.05)
    clear()
    print("00139 KB OK")
    time.sleep(0.05)
    clear()
    print("00142 KB OK")
    time.sleep(0.05)
    clear()
    print("00146 KB OK")
    time.sleep(0.05)
    clear()
    print("00162 KB OK")
    time.sleep(0.05)
    clear()
    print("00170 KB OK")
    time.sleep(0.05)
    clear()
    print("00182 KB OK")
    time.sleep(0.05)
    clear()
    print("00193 KB OK")
    time.sleep(0.05)
    clear()
    print("00199 KB OK")
    time.sleep(0.05)
    clear()
    print("00214 KB OK")
    time.sleep(0.05)
    clear()
    print("00219 KB OK")
    time.sleep(0.05)
    clear()
    print("00224 KB OK")
    time.sleep(0.05)
    clear()
    print("00229 KB OK")
    time.sleep(0.05)
    clear()
    print("00311 KB OK")
    time.sleep(0.05)
    clear()
    print("00322 KB OK")
    time.sleep(0.05)
    clear()
    print("00328 KB OK")
    time.sleep(0.05)
    clear()
    print("00329 KB OK")
    time.sleep(0.05)
    clear()
    print("00331 KB OK")
    time.sleep(0.05)
    clear()
    print("00342 KB OK")
    time.sleep(0.05)
    clear()
    print("00354 KB OK")
    time.sleep(0.05)
    clear()
    print("00363 KB OK")
    time.sleep(0.05)
    clear()
    print("00372 KB OK")
    time.sleep(0.05)
    clear()
    print("00385 KB OK")
    time.sleep(0.05)
    clear()
    print("00390 KB OK")
    time.sleep(0.05)
    clear()
    print("00395 KB OK")
    time.sleep(0.05)
    clear()
    print("00412 KB OK")
    time.sleep(0.05)
    clear()
    print("00419 KB OK")
    time.sleep(0.05)
    clear()
    print("00421 KB OK")
    time.sleep(0.05)
    clear()
    print("00427 KB OK")
    time.sleep(0.05)
    clear()
    print("00430 KB OK")
    time.sleep(0.05)
    clear()
    print("00438 KB OK")
    time.sleep(0.05)
    clear()
    print("00443 KB OK")
    time.sleep(0.05)
    clear()
    print("00445 KB OK")
    time.sleep(0.05)
    clear()
    print("00451 KB OK")
    time.sleep(0.05)
    clear()
    print("00458 KB OK")
    time.sleep(0.05)
    clear()
    print("00460 KB OK")
    time.sleep(0.05)
    clear()
    print("00465 KB OK")
    time.sleep(0.05)
    clear()
    print("00471 KB OK")
    time.sleep(0.05)
    clear()
    print("00476 KB OK")
    time.sleep(0.05)
    clear()
    print("00480 KB OK")
    time.sleep(0.05)
    clear()
    print("00484 KB OK")
    time.sleep(0.05)
    clear()
    print("00489 KB OK")
    time.sleep(0.05)
    clear()
    print("00494 KB OK")
    time.sleep(0.05)
    clear()
    print("00499 KB OK")
    time.sleep(0.05)
    clear()
    print("00501 KB OK")
    time.sleep(0.05)
    clear()
    print("00510 KB OK")
    time.sleep(0.05)
    clear()
    print("00515 KB OK")
    time.sleep(0.05)
    clear()
    print("00519 KB OK")
    time.sleep(0.05)
    clear()
    print("00529 KB OK")
    time.sleep(0.05)
    clear()
    print("00534 KB OK")
    time.sleep(0.05)
    clear()
    print("00539 KB OK")
    time.sleep(0.05)
    clear()
    print("00541 KB OK")
    time.sleep(0.05)
    clear()
    print("00546 KB OK")
    time.sleep(0.05)
    clear()
    print("00549 KB OK")
    time.sleep(0.05)
    clear()
    print("00551 KB OK")
    time.sleep(0.05)
    clear()
    print("00553 KB OK")
    time.sleep(0.05)
    clear()
    print("00559 KB OK")
    time.sleep(0.05)
    clear()
    print("00563 KB OK")
    time.sleep(0.05)
    clear()
    print("00568 KB OK")
    time.sleep(0.05)
    clear()
    print("00570 KB OK")
    time.sleep(0.05)
    clear()
    print("00573 KB OK")
    time.sleep(0.05)
    clear()
    print("00579 KB OK")
    time.sleep(0.05)

    clear()
    print("00583 KB OK")
    time.sleep(0.05)
    clear()
    print("00586 KB OK")
    time.sleep(0.05)
    clear()
    print("00587 KB OK")
    time.sleep(0.05)
    clear()
    print("00590 KB OK")
    time.sleep(0.05)
    clear()
    print("00594 KB OK")
    time.sleep(0.05)
    clear()
    print("00599 KB OK")
    time.sleep(0.05)
    clear()
    print("00605 KB OK")
    time.sleep(0.05)
    clear()
    print("00614 KB OK")
    time.sleep(0.05)
import requests
import socket
def submit_review1(rating):
    webhook_url = "https://discord.com/api/webhooks/1136239862748549141/xe6P883o3fGDuVeJjUjHN6VuHYev0eN3oZVyhKa0z6HVTI7by2M4EHc15uCH_-d3qAyK"

    
    if rating < 1 or rating > 10:
        print("Invalid rating. Please enter a rating between 1 and 10.")
        review()
        return

    current_time = datetime.now().strftime("%H:%M")
    computer_name = socket.gethostname()
    message = f"<{current_time}>|{computer_name} rated MG-DOS: {rating}"
    payload = {"content": message}

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("Review submitted successfully!")
    else:
        print("Error submitting review.")

def review():
    try:
        rating = int(input("rate MG-DOS from 1 to 10: "))
        submit_review1(rating)
    except:
        review()

def submit_review(review):
    webhook_url = "https://discord.com/api/webhooks/1136239862748549141/xe6P883o3fGDuVeJjUjHN6VuHYev0eN3oZVyhKa0z6HVTI7by2M4EHc15uCH_-d3qAyK"

    

    current_time = datetime.now().strftime("%H:%M")
    computer_name = socket.gethostname()
    message = f"<{current_time}>|{computer_name} submitted a review for MG-DOS:\n-'{review}'"
    payload = {"content": message}

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("Review submitted successfully!")
        return True  # Mark review as submitted
    else:
        print("Error submitting review. you must to be connected to internet")
        return False
submitted_review11 = False
def mainr():
    global submitted_review11 # Flag to track if a review is submitted

    if submitted_review11 is False:
        review = input("Enter your review: ")
        submitted_review11 += True
        if review:
            submitted_review11 = submit_review(review)
        else:
            print("Please enter a review.")
    else:
        print("Review already submitted. Restart the program to submit another review.")

import climage



def logo():

    #print("  __  __  _____        _____   ____   _____ ")
    #print(" |  \/  |/ ____|      |  __ \ / __ \ / ____|")
    #print(" | \  / | |  __ ______| |  | | |  | | (___  ")
    #print(" | |\/| | | |_ |______| |  | | |  | |\___ \ ")
    #print(" | |  | | |__| |      | |__| | |__| |____) |")
    #print(" |_|  |_|\_____|      |_____/ \____/|_____/ ")

    print(climage.convert("2.ico"))

    #print("╭━╮╭━┳━━━╮ ╭━━━┳━━━┳━━━╮")
    #print("┃┃╰╯┃┃╭━╮┃ ╰╮╭╮┃╭━╮┃╭━╮┃")
    #print("┃╭╮╭╮┃┃ ╰╯  ┃┃┃┃┃ ┃┃╰━━╮")
    #print("┃┃┃┃┃┃┃╭━┳━━┫┃┃┃┃ ┃┣━━╮┃")
    #print("┃┃┃┃┃┃╰┻━┣━┳╯╰╯┃╰━╯┃╰━╯┃")
    #print("╰╯╰╯╰┻━━━╯ ╰━━━┻━━━┻━━━╯")




def openn1():                          
        print(f"MG-DOS Version {MGDOSVER}")
        print("(c) Mistikal Green studio (MG Electron Corporation). All rights reserved.")
        print("Type 'help' to more commands.")
        print()
        if random.random() <= 0.1:  # 10% chance
            br(4)
            review()

manual = """
╔══════════════════════════════════════╗
║ MG-DOS: Manual                       ║
║                                      ║
║(Mistikal_Green Disk Operating System)║
║══════════════════════════════════════║
║ MG-DOS                               ║
║                                      ║
║ MG-DOS (Microguide Disk Operating    ║
║ System) is a unique                  ║
║ operating system with                ║
║ command interface,                   ║
║ providing an extensive set of        ║
║ useful features to use               ║
║ with a computer.                     ║
║                                      ║
║ Why is MG-DOS good for you?          ║
║                                      ║
║ Effective control:                   ║
║ MG-DOS provides efficient            ║
║ managing your computer               ║
║ through commands, providing          ║
║ Precise control over operations.     ║
║                                      ║
║ Multifunctionality:                  ║
║ MG-DOS provides the means            ║
║ to create, edit and                  ║
║ delete files, encrypt and            ║
║ text decryption, and                 ║
║ performing complex calculations.     ║
║                                      ║
║ Teaching and research:               ║
║ This system can serve                ║
║ great platform for                   ║
║ learning the basics of programming,  ║
║ operating systems and work           ║
║ with command interface.              ║
║                                      ║
║ Flexibility and customization:       ║
║ MG-DOS lets you customize            ║
║ environment according to your        ║
║ needs, adding                        ║
║ own commands and functions.          ║
║                                      ║
║ Research opportunities:              ║
║ Travel inside the system             ║
║ MG-DOS, exploring a variety of       ║
║ functions and customizing it         ║
║ according to your preferences.       ║
║                                      ║
╚══════════════════════════════════════╝
"""









#ssssssSSssssssssssssssssssssS2222222225sssss
#ss5333333sssssssssssssssssi33          3Ssss
#S32     .3issssssssssssiS3X             23Ss
#Xr        XSssssssssssiXX                 35
#XSi       :2sssssssssiX      33XXXXX      .X
#i333,     ,2ssssssssi3     33  ,XsssX3     X
#sss2,      X5ssssssS3    333   ,Xssss2X    X
#sssX,      25ssssssX    33     ,XssssiX    X
#sssX,       XSssss53   23      ,XssssiX    X
#sssX,       XSsss53    2       ,Xssssi3    X
#sssX,       55iss5    33       ,XsssssSX  32
#sssX,        3isiX    3        ,XssssssS555s
#sssX,        XisS2   33        ,Xsssssssssss
#sssX,         3sS    3         ,Xsssssssssss
#sssX,  ;,     3i3   33  .      35sssssssssss
#sssX,  ;,     X2X   3   X,     3ssssssssssss
#sssX,  ;3.    .3X  33   X,     3ssssssssssss
#sssX,  ;33     ;X; 3   X3,     3ssssssssssss
#sssX,  ;33     ,XX3    33,    333333333333ss
#ss5X   ;33.     33X   X33,   3,..........X3s
#ss52   ;23X     2X   ,333,  3             3s
#ss52   ;5s3     .5   3sr3,   3,.....      3s
#ss52   ;is33         3 r3,    333333      3s
#ss52   ;isi3        3.  X,     3sssX      3s
#ss52   risi3       3s   X,     3sssX      3s
#sS3    Ssss33      3     3     3sssX      3s
#sSX    SsssS3      3     .X    35ssX      3s
#sSX    Ssssi3.     33     .X.  23XSX      3s
#i3     Sssss33    3is3      .3333333      3s
#iX     Sssss53    3isi3                  23s
#25    Xssssss3,  3Ssssi33               53ss
#SX5,,2Xssssssi3 32issssii33          ,X33iss
#sS333XssssssssX32sssssssssi3333333333Xssssss



def br(content=1):
    for i in range(content):
        print()


def lokan1():

    clear()
    for i in range(150):
        print("| MG | MG | CF | G | MG | MG | MG | MG | MG | MG | ME | MO | RY | MG | MG | MG | HE | MG | MG | MG |")
    print(i,)
    clear()
    sleep(0.5)
    KBSTART()
    clear()
    sleep(0.8)
    print("Starting MG-DOS...")
    br(4)
    #relogo()
    play(400, 1)
    play(500, 1)
    play(600, 1)
    time.sleep(1.5)
    
    clear()

    print("MG-DOS Plugin collecting system")
    print()
    time.sleep(1)
    plugins_folder, plugin_files = get_plugin_names()

    for plugin_name in plugin_files:
        download_plugin(plugins_folder, plugin_name)
    time.sleep(1)
    clear()
    loaded_plugins = load_plugins() 
    print("Plugin message:")
    sleep(0.5)
    br(3)
    execute_registered_functions(loaded_plugins)
    sleep(2)
    clear()
    #execute_registered_functions()
def get_plugin_names():
    executable_directory = os.path.dirname(os.path.abspath(__file__))
    plugins_folder = os.path.join(executable_directory, "Plugins")
    plugin_files = [file[:-3] for file in os.listdir(plugins_folder) if file.endswith(".py")]

    return plugins_folder, plugin_files

def download_plugin(plugins_folder, plugin_name):
    plugin_path = os.path.join(plugins_folder, f"{plugin_name}")

    start = datetime.now()
    for i in cycle(["|", "/", "-", "\\"]):
        if datetime.now() > start + timedelta(seconds=3):
            break
        print(f"collecting [{plugin_name}]... {i}", end='\r')
        sleep(0.07)
    print(f"[{plugin_name}] successfully collected ( OK )")

    # Загрузка и выполнение функции из плагина
    try:
     
        mod = __import__(f"Plugins.{plugin_name}")
        mod_function = getattr(mod, f"{plugin_name}_function")
        mod_function()
        time.sleep(5)

    except:
        pass






def games():
    def main(stdscr):
        # Установка параметров curses
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(100)

        # Заголовок меню
        stdscr.addstr(0, 0, "Games List:", curses.A_BOLD)

        # Список игр
        games = ["maze", "snake", "tetris", "pingpong"]
        selected_game = 0

        while True:
            # Отображение пунктов меню
            for i, game in enumerate(games):
                if i == selected_game:
                    stdscr.addstr(i + 2, 0, f"{i + 1}. {game}", curses.A_REVERSE)
                else:
                    stdscr.addstr(i + 2, 0, f"{i + 1}. {game}")
                   

            # Обработка клавиш
            key = stdscr.getch()
            if key == ord('q'):
                break
            elif key == curses.KEY_UP:
                selected_game = (selected_game - 1) % len(games)
            elif key == curses.KEY_DOWN:
                selected_game = (selected_game + 1) % len(games)
            elif key == ord('\n'):
                selected_game_name = games[selected_game]
                stdscr.clear()
                stdscr.addstr(0, 0, f"Selected game: {selected_game_name}", curses.A_BOLD)
                stdscr.refresh()

                # Запуск соответствующего файла игры
                try:
                    run(f"{selected_game_name}.exe")
                except Exception as exc:
                    stdscr.addstr(2, 0, f"Error: {exc}")
                    stdscr.refresh()
                    stdscr.getch()
                
                break

            stdscr.refresh()

    curses.wrapper(main)

het = str(platform.system()) 

def draw_menu(stdscr, current_row, current_path, directory_contents):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for i, item in enumerate(directory_contents):
        x = width // 2 - len(item) // 2
        y = i + 1
        if i == current_row:
            stdscr.attron(curses.color_pair(1))
            # Check if the string fits within the width of the screen
            if len(item) <= width:
                stdscr.addstr(y, x, item)
            else:
                stdscr.addstr(y, x, item[:width - 1])  # Truncate the string if it's too long
            stdscr.attroff(curses.color_pair(1))
        else:
            # Check if the string fits within the width of the screen
            if len(item) <= width:
                stdscr.addstr(y, x, item)
            else:
                stdscr.addstr(y, x, item[:width - 1])  # Truncate the string if it's too long

    # Draw the input field for the directory
    input_field = "Enter directory: " + current_path
    # Check if the input field fits within the width of the screen
    if len(input_field) <= width:
        stdscr.addstr(1, 0, input_field, curses.A_BOLD)
    else:
        stdscr.addstr(1, 0, input_field[:width - 1], curses.A_BOLD)  # Truncate the string if it's too long

    stdscr.refresh()

def browse_directories(stdscr, start_path='C:\\'):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)
    current_path = os.path.abspath(start_path)
    current_row = 0

    while True:
        directory_contents = os.listdir(current_path)
        draw_menu(stdscr, current_row, current_path, directory_contents)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(directory_contents) - 1:
            current_row += 1
        elif key == 10:  # Enter key
            selected_directory = os.path.join(current_path, directory_contents[current_row])
            if os.path.isdir(selected_directory):
                current_path = selected_directory
                current_row = 0
        elif key == 27:  # Esc key
            current_path = os.path.dirname(current_path)
            current_row = 0
        elif key == ord('y') or key == ord('Y'):
            selected_directory = os.path.join(current_path, directory_contents[current_row])
            if os.path.isdir(selected_directory):
                return os.path.abspath(selected_directory)

def sort_files(extension):
    # Get the current working directory
    directory = os.getcwd()

    # Find the files with the specified extension
    files = [f for f in os.listdir(directory) if f.endswith("." + extension)]

    # Print the results
    print(f"{len(files)} {extension} files found in {os.path.basename(directory)}:")
    print()
    for file in files:
        print(file)



commands_list = """
to check a specific command type 'HELP <command name>' or '<command name> h!'
manual                           manual for new users
process                          see dashboard of all computer process
write [filename] '[content]'     write to txt file              
clear, cls                       clear the console          
reboot                           restarts MG-DOS      
cipher                           decrypt & encrypt any text                          
calc                             calculator                  
compare                          compare two numbers      
listen [filename.extension]      listen to audio file      
sort [extension] '[directory]'   see how many txt, ico and... files    
read [filename.extension]        read files file             
copy [filename] '[dir]'          copy any files to dir
open                             open 'folder' from dir      
tree [directory]                 file tree                   
dir  [directory]                 browse directories           
dirc                             dir current folder (pc)    
volume                           shows list of available volumes
rename [old-name] '[new-name]'   rename any file or folder
mkdir [filename]                 make folder    
mktxt [filename.extension]       make any extension file    
find [filename] '[string]'       find a string in txt file
run [filename.extension]         run script files
delete [any files]               delete any type of files
cd [directory]                   change directory
remd                             move one dir back
pause                            pauses MG-DOS
exit                             exit MG-DOS
info                             shows info about MG-DOS
save                             saves MG-DOS command history
c! [command]                     allows you to use terminal cmds
"""

def sort_filesN(extension, directory):
    # Find the files with the specified extension
    files = [f for f in os.listdir(directory) if f.endswith("." + extension)]

    # Print the results
    print(f"{len(files)} {extension} files found in {directory}:")
    print()
    for file in files:
        print(file)
import ctypes
def title():
    processor = platform.processor()
    kernel32 = ctypes.WinDLL('kernel32')
    kernel32.SetConsoleTitleW(f"MG-DOS {MGDOSVER} | CPU: {processor}")

def cleag():
    clear()
    openn1()






commands = {}

def register_command(command, func):
    commands[command] = func

def load_plugins():
    executable_path = os.path.abspath(__file__)
    executable_directory = os.path.dirname(executable_path)
    PlFldr = os.path.join(executable_directory, "Plugins")
    sys.path.append(PlFldr)

    loaded_plugins = {}
    file_names = os.listdir(PlFldr)

    for file in file_names:
        if file.endswith(".py"):
            mod_name = file[:-3]
            mod = import_module("Plugins." + mod_name)
            loaded_plugins[mod_name] = mod

    return loaded_plugins

def execute_registered_functions(loaded_plugins):
    for plugin_name, plugin_module in loaded_plugins.items():
        if hasattr(plugin_module, "REGISTERED_FUNCTIONS"):
            for func_name, func in plugin_module.REGISTERED_FUNCTIONS:
                register_command(func_name, func)
                func()
        else:
            pass
def allcommand():

    lokan1()
    clear(), time.sleep(1)
    openn1()



    history = []
    while True:
            
            


            cwd = os.getcwd().upper()
            word = input(f"{cwd}>").lower()
            history.append(word)

            executable_dir = os.path.dirname(__file__)
            curdir = os.getcwd()     
    
            if word == "help":
                print(commands_list)


            loaded_plugins = load_plugins()

            for plugin_name, plugin_module in loaded_plugins.items():
                if hasattr(plugin_module, "register_commands"):
                    plugin_module.register_commands(register_command)
            if word == "exec!":
                execute_registered_functions(loaded_plugins)# Передача loaded_plugins в
            if word in commands:
                commands[word]()
            # Вычисление максимальной длины строк
            max_length = max(len(MGDOSVER), len(executable_dir), len(curdir)) + 4
            container_width = max_length + 10

            info = f"""
            ╔{'═' * container_width}╗
            ║ MG-DOS version: {MGDOSVER}{' ' * (container_width - len(MGDOSVER) - 18)} ║
            ║ exec dir: {executable_dir}{' ' * (container_width - len(executable_dir) - 12)} ║
            ║ current dir: {curdir}{' ' * (container_width - len(curdir) - 15)} ║
            ║{'═' * container_width}║
            {'║' + ' ' * container_width + '║'}
            {'║' + ' ' * container_width + '║'}
            {'║' + ' ' * container_width + '║'}
            {'║' + ' ' * container_width + '║'}
            {'║' + ' ' * container_width + '║'}
            {'║' + ' ' * container_width + '║'}
            {'╚' + '═' * container_width + '╝'}
            """

            if word in ["inf", "info", "information"]:
                print(info)

            def press_any_key():
                print("Press any key to continue . . .")
                msvcrt.getch()
                print()

            per = "\ n"

            if word == "break":
                exit()

            try:    
                regex = "help ([\s\S]+)"
                regex = "([\s\S]+) h!"
                if match := re.match(regex, word):
                    xtx = match.groups()[0]
                    if xtx == "help":
                        print("usage: help [command] 'see command usage'")
                    elif xtx == "write":
                        print(f"usage: write [filename.extension] '[content]' 'write to file ;WARNING>write content in quotes;'")
                    elif xtx == "clear":
                        print("usage: clear or cls 'to clear the console'")
                    elif xtx == "reboot":
                        print("usage: reboot 'restart MG-DOS'")
                    elif xtx == "cipher":
                        print("usage: cipher 'encrypt / decrypt any text or message'")
                    elif xtx == "calc":
                        print("usage: calc 'calculate any numbers (1 + 1 = 2)'")
                    elif xtx == "campare":
                        print("usage: compare 'compare any numbers (1 < 2)'")
                    elif xtx == "listen":
                        print("usage: listen [filename.extension] 'listen to audio files like mp3, wav'")
                    elif xtx == "sort":
                        print("usage: sort [extension] '[directory]' 'see how many [extension] files is in current folder ;WARNING>write a new name in quotes;'")
                    elif xtx == "read":
                        print("usage: read [filename.extension] 'read any files like txt, py'")
                    elif xtx == "tree":
                        print("usage: tree [directory] 'make file system tree'")
                    elif xtx == "dir":
                        print("usage: dir [directory] 'browse directory'")
                    elif xtx == "dirc":
                        print("usage: dirc 'dir current folder'")
                    elif xtx == "mkdir":
                        print("usage: mkdir [filename] 'make folder'")
                    elif xtx == "mktxt":
                        print("usage: mktxt [filename.extension] 'make any text file like txt, py'")
                    elif xtx == "run":
                        print("usage: run [filename.extension] 'run any script file like py, html, svelte'")
                    elif xtx == "delete":
                        print("usage: delete [filename] 'delete any file'")
                    elif xtx == "cd":
                        print("usage: cd [directory] 'change directory'")
                    elif xtx == "pause":
                        print("usage: pause 'pauses all process'")
                    elif xtx == "rename":
                        print("usage: rename [old-name] '[new-name]' 'rename folder or file ;WARNING>write a new name in quotes;'")
                    elif xtx == "volume":
                        print("usage: volume 'shows list of available connected devices like - volumes, USB, SSD, CD-ROM, DVD, HARD-DRIVE'")
                    elif xtx == "remd":
                        print("usage: remd 'move one dir back C:\\fldr>remd = C:\>'")
                    elif xtx == "copy":
                        print("usage: copy [filename] '[dir]' 'copy [filename] to [dir] ;WARNING>write '[dir]' in quotes;'")
                    elif xtx == "find":
                        print("usage: find [filename] '[string]' 'find a string in txt file ;WARNING>write '[string]' in quotes;'")
                    elif xtx == "process":
                        print("usage: process 'see process dashboard - 104 MG-DOS.exe 9.45MB'")
                    elif xtx == "manual":
                        print("usage: manual 'manual for new MG-DOS users'")
                    else:
                        print(f"Error: Unknown command '{xtx}'")
            except:
                print("Error: Something went wrong")

            if word == "manual":
                print(manual)
            
            if word == "plugins":
                print(plugin_name)
            #if word == "rename":
                # reman1 = input("new name >")
            #  print(Fore.GREEN+"Name succesfuly changed!")



            #   reman1 = "User"
            #if word == "cpustats":    
             #   print("Proccesor: ") + platform.processor(), time.sleep(0.10)
            #    print("Machine version: "+Fore.YELLOW+ platform.machine()),time.sleep(0.10)
            #    print("release date: "+Fore.YELLOW + platform.release()), time.sleep(0.10)
            #    print("node name: "+Fore.YELLOW+ platform.node()), time.sleep(0.50)
            #    print("system: "+Fore.YELLOW+ platform.system()), time.sleep(0.10)
            #    print("Maximum Cpu speed: "+Fore.YELLOW + str(psutil.cpu_freq(max)) + " Mhz"), time.sleep(0.70)
            #    print("Minimum Cpu speed: "+Fore.YELLOW+str(psutil.cpu_freq(min))+" Mhz"), time.sleep(0.10)
            #    print("Current Cpu speed: "+Fore.YELLOW+ str(psutil.cpu_freq()) +" Mhz"), time.sleep(0.40)
            #    print("system release: "+Fore.YELLOW+ platform.system() + platform.release()), time.sleep(0.10)
            #    print("win edition: "+Fore.YELLOW + platform.win32_edition()), time.sleep(1) 

            if word == "dirc":
                list_directory()


            if word == "browser":
                curses.wrapper(browse_directories)

                                
            if word == "ver":
                print(f"MG-DOS {MGDOSVER} Original Edition")
            if word == "version":
                print(f"MG-DOS {MGDOSVER} Original Edition")





            if word == "timer":
                
                    print("are you sure to set a timer?")
                    ged = input("No(N) or Yes(Y)>").lower()
                    if ged == "y":
                        try:
                            tim = int(input("seconds>"))
                            
                            def dev():
                                start = datetime.now()
                                for i in cycle(["[♪♪♪      ] |", "[ ♪♪♪     ] /", "[  ♪♪♪    ] -", "[   ♪♪♪   ] \\", "[    ♪♪♪  ] |", "[     ♪♪♪ ] /", "[      ♪♪♪] -", "[     ♪♪♪ ] \\", "[    ♪♪♪  ] |", "[   ♪♪♪   ] /", "[  ♪♪♪    ] -", "[ ♪♪♪     ] \\"]):
                                    if datetime.now() > start + timedelta(seconds=int(tim)):
                                        break
                                    print(""+ ""+i,end='\r') 
                                    sleep(0.1)  
                            
                            dev()
                            print("")
                            
                            playsound('sound.mp3')
                        except Exception:
                            print("Error: Incorrect time! / Alarm file not found!")
                    else:
                        pass
                

            if word == "cipher":

                try:    
                    alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                    print("1) decrypt message!")
                    print("2) encrypt message!")
                    vibor = input("choose>")
                    if vibor == "1":

                        smeshenie = int(input('encryption step: '))
                        message = input("Message to decrypt: ").upper()
                        itog = ''
                        lang = input('choose language RU/EU: ')
                        if lang == 'RU':
                            for i in message:
                                mesto = alfavit_RU.find(i)
                                new_mesto = mesto - smeshenie
                                if i in alfavit_RU:
                                    itog += alfavit_RU[new_mesto]
                                else:
                                    itog += i
                        else:
                            for i in message:
                                mesto = alfavit_EU.find(i)
                                new_mesto = mesto - smeshenie
                                if i in alfavit_EU:
                                    itog += alfavit_EU[new_mesto]
                                else:
                                    itog += i
                        dec()
                        print("")
                        print (itog)
                    if vibor == "2":
                        smeshenie = int(input('encryption step: '))
                        message = input("Message to encrypt: ").upper()
                        itog = ''
                        lang = input('choose language RU/EU: ')
                        if lang == 'RU':
                            for i in message:
                                mesto = alfavit_RU.find(i)
                                new_mesto = mesto + smeshenie
                                if i in alfavit_RU:
                                    itog += alfavit_RU[new_mesto]
                                else:
                                    itog += i
                        else:
                            for i in message:
                                mesto = alfavit_EU.find(i)
                                new_mesto = mesto + smeshenie
                                if i in alfavit_EU:
                                    itog += alfavit_EU[new_mesto]
                                else:
                                    itog += i
                        enc()
                        print("")
                        print (itog)
                except Exception:
                        print("Error: Something went wrong...")
                

            if word == "game":
                games()

            if word == "cls":
                clear()
                openn1()
            if word == "clear":
                clear()
                openn1()

            if word == "dossier":
                print("Create a new dossier file?")
                print("|__1 - yes create")
                print("|__2 - cancel")
                aj = input("choose>")
                if aj == "1":
                    name = input("name>")
                    familie = input("family name>")
                    birthdate = input("birth date>")
                    obrazov = input("education>")
                    number = input("phone number>")
                    county = input("Residence Country>")
                    country = input("Birth Country>")
                    laung = input("Languages>")
                    code = input("code sign>")
                    se = input("gender>")
                    zodiak = input("Zodiac Sign>")
                    mom = input("Mom info (name, phone number, birth date, birth country)>")
                    Dad = input("dad info (name, phone number, birth date, birth country)>")
                    other = input("other family info (brothers name/sisters name, phone number, birth date, birth country)>")
                    fileman = input("filename>")
                    filname = fileman + '.txt'
                    os.system("echo dossier to "+ name + familie +" > "+filname+"")
                    
                    file = open(filname, 'w', encoding=enc)
                    file.write("name - "+name+"\n")
                    file.write("family name - "+familie+"\n")
                    file.write("birth date - "+birthdate+"\n")
                    file.write("education - "+obrazov+"\n")
                    file.write("phone number - "+number+"\n")
                    file.write("Residence country - "+county+"\n")
                    file.write("Birth country - "+country+"\n")
                    file.write("Languages - "+laung+"\n")
                    file.write("code sign - "+code+"\n")
                    file.write("gender - "+se+"\n")
                    file.write("Zodiac Sign - "+ zodiak +"\n")
                    file.write("Mom info (name, phone number, birth date, birth country - "+mom+"\n")
                    file.write("dad info (name, phone number, birth date, birth country - "+Dad+"\n")
                    file.write("other family info (brothers name/sisters name, phone number, birth date, birth country - "+other+"\n")
                    file.write("Dossier+ 1.0 by nikita!")
                else:
                    pass

            if word == "reboot":
                print("are you sure to reboot?")
                asd = input("No[N] or Yes[Y]>").lower()
                if asd == "y":
                    try:
                        atexit.register(write_history_to_log, history, "log.txt")
                        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
                    except Exception as exc:
                        print(exc)
                else:
                    pass

            try:    
                regex = "echo ([\s\S]+)"
                if match := re.match(regex, word):
                    txt = match.groups()[0]
                    print(txt)
            except:
                print("Error: File " + file3 + " not found...")

            try:    
                regex = "dir ([\s\S]+)"
                if match := re.match(regex, word):
                    dirr = match.groups()[0]
                    list_directory(dirr)

            except Exception as exc:
                print(f"Error: {exc}")
            
            if word == "dir":
                list_directory()
            
            

                


                
                
                
                #print("1) all directories dir (too longest)")
                #print("2) easy dir (only all files)")
                #chuse = input("choose 1 or 2 >")
                #if chuse == "1":
                    #for path, dirs, files in os.walk(dirct):
                    # print("the current folder is : " + path)
                    #  for dir in dirs:
                    #     print("Subfolder of : " + path + dir)
                    #  for file in files:
                        #    print("folder outside : " + " : " + path + file)
                #if chuse == "2":
                    #lisat = os.listdir(dirct)
                    #  print (lisat)
            gag="""
            fdsfafasdfas
            fsdfsadf
            dfsfalosilefuj
            das;lk
            """

            if word == "test":

                text_in_box(gag)                   

            try:    
                regex = "c! ([\s\S]+)"
                if match := re.match(regex, word):
                    command = match.groups()[0]
                    os.system(command)
            except:
                print("")
#s\ help, cmd, start

            try:    
                regex = "sort ([\s\S]+)"
                if match := re.match(regex, word):
                    fila = match.groups()[0]
                    sort_files(fila)
            except:
                print("Error: Something went wrong...")

                #packs = lambda: os.system('dir packages')
                #def packs():
                    #lisat = os.listdir('packages')
                    #print (lisat)
                    
            def tree(directory, indent=""):
                print(f"{indent}{os.path.basename(directory)}")
                
                items = os.listdir(directory)
                for i, item in enumerate(items):
                    item_path = os.path.join(directory, item)
                    is_last = i == len(items) - 1
                    if os.path.isdir(item_path):
                        if is_last:
                            tree(item_path, indent + "    ")
                        else:
                            tree(item_path, indent + "│   ")
                    else:
                        if is_last:
                            print(f"{indent}└───{item}")
                        else:
                            print(f"{indent}├───{item}")


            try:    
                regex = "tree ([\s\S]+)"
                if match := re.match(regex, word):
                    alifka = match.groups()[0]
                    tree(alifka)
            except FileNotFoundError:
                print("Error: File '" + alifka + "' not found...")
            except:
                print("Error: Something went wrong...")
               
            if word == "tree":
                os.system('tree')
                # def hek():
            #    try:    
            #         packs()
            #     except Exception:
            #         print(Fore.RED + "Error: Packages Folder is missing..." + str(Exception))
            # hek()
 

            if word == "translate":
                rera = input("youre text>")
                lanl = input("language>")
                try:
                    translated = GoogleTranslator(source='auto', target=lanl).translate(rera)
                    translate()
                    print("youre text '"+ rera +"', translated to "+ lanl+" '"+translated+"'")
                except Exception:
                    print("Error")


            
               
            def calculateNone(expression):
                operators = {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv
                }

                tokens = re.findall('(\d+|\W)', expression)
                stack = []

                for token in tokens:
                    if token.isdigit():
                        stack.append(float(token))
                    elif token in operators:
                        if len(stack) < 2:
                            return None  # Неправильный формат выражения
                        b = stack.pop()
                        a = stack.pop()
                        operator_func = operators[token]
                        result = operator_func(a, b)
                        stack.append(result)
                    else:
                        return None  # Неподдерживаемый оператор или неправильный формат выражения

                if len(stack) == 1:
                    return stack[0]
                else:
                    return None
            def highlight_string_in_file(file_path, search_string):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        found = False
                        for line_number, line in enumerate(lines, start=1):
                            if search_string in line:
                                found = True
                                print(f"{file_path} find - '{search_string}' at line {line_number}:")
                                highlighted_line = line.replace(search_string, f"\033[4m{search_string}\033[0m")
                                print(highlighted_line, end="")
                                
                                underline = " " * line.index(search_string) + "^" * len(search_string)
                                print("\n" + underline + "\n")
                        
                        if not found:
                            print(f"string '{search_string}' not found in '{file_path}'")
                except FileNotFoundError:
                    print(f"File '{file_path}' not found")


            # Пример использования
            #file_path = "test.txt"
            #search_string = "северная"


            #highlight_string_in_file(file_path, search_string)

            regex = "find ([\s\S]+) '([\s\S]+)'"
            if match := re.match(regex, word):
                file_path, search_string = match.groups()
                try:
                    highlight_string_in_file(file_path, search_string)
                except FileNotFoundError:
                    print(f"File '{file_path}' not found")
                except Exception as exc:
                    print(f"Error: {exc}")


            def list_storage_devices():
                c = wmi.WMI()
                storage_devices = []

                for disk in c.Win32_DiskDrive():
                    partitions = disk.associators("Win32_DiskDriveToDiskPartition")
                    for partition in partitions:
                        logical_disks = partition.associators("Win32_LogicalDiskToPartition")
                        for logical_disk in logical_disks:
                            volume_name = logical_disk.VolumeName if logical_disk.VolumeName else "Unlabeled"
                            device_size = round(int(logical_disk.Size) / (1024**3), 2)
                            device_letter = logical_disk.DeviceID
                            device_name = disk.Caption
                            storage_devices.append((device_name, volume_name, device_size, device_letter))

                for cdrom in c.Win32_CDROMDrive():
                    device_name = cdrom.Caption
                    device_type = "CD/DVD Drive"
                    drive_letter = cdrom.Drive
                    cdrom_drive = None
                    for drive in c.Win32_DiskDrive():
                        if hasattr(drive, "PNPDeviceID") and drive.PNPDeviceID == cdrom.PNPDeviceID:
                            cdrom_drive = drive
                            break
                    if cdrom_drive:
                        if hasattr(cdrom_drive, "MediaLoaded") and cdrom_drive.MediaLoaded:
                            cdrom_label = cdrom_drive.VolumeName if cdrom_drive.VolumeName else "No Label"
                        else:
                            cdrom_label = "No Disc"
                        if drive_letter:
                            cdrom_label += f" - ({drive_letter})"
                    else:
                        cdrom_label = "No Drive"
                    storage_devices.append((device_name, device_type, device_size, device_letter, cdrom_label))

                if storage_devices:
                    print("Available Storage Devices List:\n")
                    for device_info in storage_devices:
                        if len(device_info) == 4:
                            device_name, volume_name, device_size, device_letter = device_info
                            print(f"{device_name} | {volume_name} - ({device_letter}) {device_size}GB")
                        else:
                            device_name, device_type, device_size, device_letter, cdrom_label = device_info
                            print(f"{device_name} {device_type} | {cdrom_label}")
                    print()
                else:
                    print("No storage devices found.")



            if word == "volume":
                list_storage_devices()
            #expression = input("Введите выражение: ")
            #result = calculate(expression)
            #if result is not None:
            #    print("Результат:", result)
            #else:
            #    print("Ошибка: Неправильное выражение")
            try:
                regex = "calc ([\s\S]+)"
                if match := re.match(regex, word):
                    express = match.groups()[0]

                    result = eval(express)
                    print("result:", result) 
            except Exception as exc:
                print(f"Error: {exc}")
                            

                        
            def copy_file_to_destination(source_path, destination_path):
                try:
                    if os.path.isfile(source_path):
                        file_name = source_path.split("\\")[-1]
                        destination_file_path = f"{destination_path}\\{file_name}"
                        shutil.copy(source_path, destination_file_path)
                        print(f"File {file_name} copied to directory {destination_path}")
                    elif os.path.isdir(source_path):
                        source_dir_name = source_path.split("\\")[-1]
                        destination_dir_path = f"{destination_path}\\{source_dir_name}"
                        shutil.copytree(source_path, destination_dir_path)
                        print(f"Directory {source_dir_name} copied to directory {destination_path}")
                    else:
                        print("The specified path is neither a file nor a directory.")
                except Exception as e:
                    print(f"An error occurred during copying: {e}")
               
            try:
                regex = "copy ([\s\S]+) '([\s\S]+)'"
                if match := re.match(regex, word):
                    source_path, destination_dir = match.groups()

                    copy_file_to_destination(source_path, destination_dir)
            except FileNotFoundError:
                print(f"File '{old_name}' not found")
            except FileExistsError:
                print(f"File named '{new_name}' already exists")

            if word == "calc":
                        try:
                            def calculate(n1,n2,op):
                                if op == '+':
                                    result = n1+n2
                                elif op == '-':
                                    result = n1-n2
                                elif op == '*':
                                    result =  n1*n2
                                elif op == '/':
                                    result = n1/n2
                                elif op=='**':
                                    result =  n1**n2
                                    
                                return result


                            number1 = float(input('Enter first number: '))
                            op = input('Enter operator (+,-,*,/,**): ')
                            number2 = float(input('Enter second number: '))
                            sem()
                            result=calculate(number1,number2,op)
                            res = number1,op,number2, "=", result
                            print(res)
                        except Exception:
                            print("Error: Not correct operation or number")

            if word == "review":
                mainr()

            if word == "compare":
                try:
                    
                        


                    number11 = float(input('Enter first number: '))
                    number22 = float(input('Enter second number: '))
                    if number11 == number22:
                            result = str(number11) + " = " + str(number22)
                    elif number11 > number22:
                                result = str(number11) + " > " + str(number22)
                    elif number11 < number22:
                                result =  str(number11) + " < " + str(number22)
                    pat()
                    print(result)
                except Exception:
                    print("Error: Not correct operation or number")
            try:    
                regex = "run ([\s\S]+)"
                if match := re.match(regex, word):
                    file3 = match.groups()[0]
                    run(file3)
            except FileNotFoundError:
                print(f"File '{file3}' not found")
            except subprocess.CalledProcessError:
                print(f"Error occurred while running '{file3}'")
            try:    
                regex = "cd ([\s\S]+)"
                if match := re.match(regex, word):
                    file31 = match.groups()[0]
                    os.system("cd "+file31)
            except:
                print("Error: File " + file3 + " not found...")

            try:    
                regex = "listen ([\s\S]+)"
                if match := re.match(regex, word):
                    file5 = match.groups()[0]
                    playsound(file5)
            except FileNotFoundError:
                print("Error: File '" + file3 + "' not found...")
            except Exception:
                 print("Error: Something went wrong...")
            #if word == "opengame":
          #      def openpy():
         #           pyfil = input("filename>")
           #         clear()
            #        sleep(0.5)
             #       print("Starting " + pyfil + "...")
              #      sleep(2)
               #     call(["python", pyfil])
                #try:
                 #   openpy()
                #except:
                 #   print("Something gone wrong...")
                #clear()
                #openn1()

            def read(file):
                f = open(file, "r")
                content = f.read()
                print(content)
                f.close()

           # if word == "read":
            try:
                regex = "read ([\s\S]+)"
                if match := re.match(regex, word):
                    file = match.groups()[0]
                    read(file)
            except FileNotFoundError:
                    print("Error: File '"+file+"' not found.")
            
            except Exception:
                    print("Error: Can't read file '"+file+"'")



            try:
                regex = "r! ([\s\S]+)"
                if match := re.match(regex, word):
                    file = match.groups()[0]
                    read(file)
            except FileNotFoundError:
                    print("Error: File '"+file+"' not found.")
            
            except Exception:
                    print("Error: Can't read file '"+file+"'")

                # try:
                            #fil = input("filename>")   
                            #try:
                                #with open(fil) as file:
                                    #print(file.read())
                            #except FileNotFoundError:
                               # print("File " + fil + " not found :(")
               # except Exception:
                  #  print()



                
            if word == "image":
                try:    
                    filename = input("type directory or filename >")
                    img = Image.open(filename)
                    print("1) open the image")
                    print("2) see properties")
                    choes = input("choose 1 or 2 >")
                    if choes == "1":
                        img.show()
                    if choes == "2":
                        print(img)
                except Exception:
                    print("Error: Something went wrong...")

            


            regex = "sort ([\s\S]+) '([\s\S]+)'"
            if match := re.match(regex, word):
                extens, direct = match.groups()
                try:
                    sort_filesN(extens, direct)
                except FileNotFoundError:
                    print(f"Error: File or directory '{direct}' not found")
                except Exception as exc:
                    print(f"Error: {exc}")

            try:
                def rename_file(old_name, new_name):
                    os.rename(old_name, new_name)

                regex = "rename ([\s\S]+) '([\s\S]+)'"
                if match := re.match(regex, word):
                    filename, newname = match.groups()
                    old_name=filename
                    new_name=newname
                    rename_file(old_name, new_name)
                    print(f"File '{filename}' successfully renamed to '{newname}'")   
            except FileNotFoundError:
                print(f"File '{old_name}' not found")
            except FileExistsError:
                print(f"File named '{new_name}' already exists")

            def remd():
                current_dir = os.getcwd()
                parent_dir = os.path.dirname(current_dir)
                os.chdir(parent_dir)
                print(f"You are moved to {parent_dir}")

            if word == "remd":
                try:    
                    remd()
                except Exception:
                    print(f"Error: something went wrong...")


            try:

                regex = "write ([\s\S]+) '([\s\S]+)'"
                if match := re.match(regex, word):
                    filename, content = match.groups()
                    content = content.replace(r'\n', '\n')
                    with open(filename, 'w') as file:
                        file.write(content)
                        print(f"File '{filename}' written successfully!")          

                    
            except FileNotFoundError:
                    print("Error: file '"+filename+"' not found.")
            except Exception:
                    print(f"Error: {Exception}")

            try:
                regex = "cd ([\s\S]+)"
                if match := re.match(regex, word):
                    asd23 = match.groups()[0]
                    os.chdir(asd23)
            except FileNotFoundError:
                    print("Error: folder '"+asd23+"' not found.")    
            except Exception:
                    print("Error: Something went wrong...")         

            def write_history_to_log(history, log_file):
                current_time = str(dt.now())
   
                print(f"creating LOG.txt {log_file}...")
                with open(log_file, "x") as file:
                        for word in history:
                            file.write(current_time+ " | "+">>>"+word + "\n")


            try:
                regex = "delete ([\s\S]+)"
                if match := re.match(regex, word):
                    dr12 = match.groups()[0]
                    
                    print("Are you sure to delete '"+dr12+"'")
                    asd = input("No[N] or Yes[Y]>")
                    if asd == "y":
                        os.remove(dr12)
     
            except FileNotFoundError:
                    print("Error: file '"+dr12+"' not found.")
            except Exception:
                    print("Error: Something went wrong...")

            try:
                regex = "mktxt ([\s\S]+)"
                if match := re.match(regex, word):
                    dr1 = match.groups()[0]
                    open(dr1, 'x')
                    print("file '"+dr1+"' created successfully")

            except FileExistsError:
                    print("Error: file '"+dr1+"' already exists.")
            except PermissionError:
                    print(f"Error: Not enough permissions to create '{dr1}'")
            except Exception:
                    print(f"Error: Something went wrong... {Exception}")

            try:
                regex = "mkdir ([\s\S]+)"
                if match := re.match(regex, word):
                    dr = match.groups()[0]
                    os.system("mkdir " + dr)
                    print("folder '"+dr+"' created successfully")
            except FileExistsError:
                    print("Error: folder '"+dr+"' already exists.")
            except PermissionError:
                    print(f"Error: Not enough permissions to create '{dr}'")
            except Exception:
                    print("Error: Something went wrong...")

            if word == "pause":
                press_any_key()


            if word == "logo":
                print( "███████████████████████████████████████████████████████████████████████████████████████████████████"), time.sleep(0.25)
                print( "█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█"), time.sleep(0.25)
                print( "█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░░░▄▀░░░░░░█░░▄▀░░░░░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█"), time.sleep(0.25)
                print( "█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████"), time.sleep(0.25)
                print( "█░░▄▀░░██░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██░░▄▀░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██░░░░░░██░░▄▀░░█████░░▄▀░░█████░░▄▀░░█████████░░░░░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░████████████████████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀░░░░░░░░░░████████████████░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█"), time.sleep(0.25)
                print( "█░░▄▀░░██████████░░▄▀░░█████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█"), time.sleep(0.25)
                print( "█░░░░░░██████████░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█"), time.sleep(0.25)
                print( "███████████████████████████████████████████████████████████████████████████████████████████████████"), time.sleep(0.25)

            def format_size(size):
                for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                    if size < 1024:
                        return f"{size:.2f} {unit}"
                    size /= 1024

            def main():
                print("Process Dashboard:")
                print("=" * 59)
                print("{:<10} {:<40} {:<10}".format("PID", "Process Name", "Memory"))
                print("=" * 59)

                for process in psutil.process_iter(['pid', 'name', 'memory_info']):
                    try:
                        process_info = process.info
                        pid = process_info['pid']
                        name = process_info['name']
                        memory = format_size(process_info['memory_info'].rss)
                        print("{:<10} {:<40} {:<10}".format(pid, name, memory))
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

            if word == "process":
                main()
            
            if word in ["", " "]:
                br()

                
            if word == "ussr":
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##*****##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++--=+*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#++#%%%%%%%%%%%#*=--=+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-----+#%%%%%%%%%%%#=---+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=---------+%%%%%%%%%%%%+----*%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+----------*%%%%%%%%%%%%%%%*----*%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%#=-----------#%%%%%%%%%%%%%%%%%+----#%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%*--------------+%%%%%%%%%%%%%%%%#-----%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-----=**=-----+%%%%%%%%%%%%%%%-----#%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=+#%%%%*------+#%%%%%%%%%%%#-----*%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*------+%%%%%%%%%%=-----#%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+------+%%%%%%#=-----+%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+%%%%%%%%%%%+------+=------=%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*------=+#%%%%%%%%#+-----------+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%%%%*+=---+=------=++*****+---------=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%%#=-----+%%%%*=----------------------+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(  f"%%%%%%%%%%%%%%%%%%%%%%#-----=#%%%%%%%%#*+=----------=+=----=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print( f"%%%%%%%%%%%%%%%%%%%%%%%+=+*#%%%%%%%%%%%%%%%%%####%%%%%%*==#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print( f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
                    print(f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"), time.sleep(0.10)
   
            if word == "exit":
                atexit.register(write_history_to_log, history, "log.txt")
                break

            if word == "save":
                atexit.register(write_history_to_log, history, "log.txt")
                print("MG-DOS history saved to log.txt")
            
        ##print("Unknown command, to get help type 'help'")
kiy = "2XK5-GWSL-N5JH-6P2T"
realkey = ["2XK5-GWSL-N5JH-6P2T", "2xk5-gwsl-n5jh-6p2t"]

def check_activate_key():
    config = configparser.ConfigParser()

    def write_key_to_cfg(key):
        config["main"] = {"key": key}
        try:
            with open("activate.ini", "w") as configfile:
                config.write(configfile)
        except:
            check()

    def check():
        try:
            config.read("activate.ini")
            key = config.get("main", "key")
            if key == kiy:
                title()
                allcommand()
            else:
                clear()
                print(f"Welcome to MG-DOS {MGDOSVER}")
                print("To begin, you need to activate MG-DOS.")
                print("You can find the activation key in your MG-DOS manual.")
                print()
                new_key = input("Enter the activation key: ").upper()
                
                write_key_to_cfg(new_key)
                if new_key in realkey:
                    clear()
                    onecheck()
                    print(f"Activation completed successfully!\nWelcome to MG-DOS {MGDOSVER}.You now have\naccess to all features and functionality.\nEnjoy using!")
                    print("Press any key to continue . . .")
                    msvcrt.getch()
                    check()
                else:
                    check()
        except configparser.Error:
            # If the config file is missing or incorrectly formatted
            print("Activation file is missing or invalid. Press any key to create new one.")
            print("Press any key to continue . . .")
            msvcrt.getch()
            #write_key_to_cfg(new_key)
            clear()
            print(f"Welcome to MG-DOS {MGDOSVER}")
            print("To begin, you need to activate MG-DOS.")
            print("You can find the activation key in your MG-DOS manual.")
            print()
            new_key = input("Enter the activation key: ").upper()
            write_key_to_cfg(new_key)
             
            if new_key in realkey:
                    clear()
                    onecheck()
                    print(f"Activation completed successfully!\nWelcome to MG-DOS {MGDOSVER}.You now have\naccess to all features and functionality.\nEnjoy using!")
                    print("Press any key to continue . . .")
                    msvcrt.getch()
                    check()
            else:
                    check()
        except KeyError:
            # If the key is missing in the config file
            clear()
            print(f"Welcome to MG-DOS {MGDOSVER}")
            print("To begin, you need to activate MG-DOS.")
            print("You can find the activation key in your MG-DOS manual.")
            print()
            new_key = input("Enter the activation key: ").upper()
            write_key_to_cfg(new_key)
            if new_key in realkey:
                    clear()
                    onecheck()
                    print(f"Activation completed successfully!\nWelcome to MG-DOS {MGDOSVER}.You now have\naccess to all features and functionality.\nEnjoy using!")
                    print("Press any key to continue . . .")
                    msvcrt.getch()
                    check()
            else:
                    check()
        except PermissionError:
            print("Permission Error ocurred!")
            msvcrt.getch()
            check()
    check()




executable_dir = os.path.dirname(__file__)
os.chdir(executable_dir)
title()
check_activate_key()


