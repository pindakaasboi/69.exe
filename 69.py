import tkinter as tk
from tkinter import messagebox
import webbrowser
import win32gui
import win32con
import win32api
import win32ui
import random
import ctypes
import time
import numpy as np
import sounddevice as sd
import ctypes
import random
from win32api import *
from win32con import *
from win32gui import *
from tkinter import *
import time
import sys

def open_link():
    webbrowser.open('https://nl.pornhub.com/')  # Replace 'https://www.example.com' with your desired link

def display_msgbox():
    messagebox.showinfo("From 69.exe", "i hope this something for you!")
    open_link()

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Display the message box and open the link
display_msgbox()

time.sleep(3.4)

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


x = y = 0
for _ in range(10000):
    win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR)) # Change IDI_ERROR to something else to change the icon being displayed
    x = x + 30
    if x >= w:
        y = y + 30
        x = 0
    if y >= h:
        x = y = 0

def bytebeat(t):
    # Replace this with your bytebeat formula
    return t & 0xFF  # Ensure the result is within 8-bit range

duration = 600  # Duration of the audio (in seconds)
sample_rate = 7000  # Sample rate (adjust as needed)

t_values = np.arange(0, duration * sample_rate)
audio_data = np.array([bytebeat(t) for t in t_values], dtype=np.int8)  # Change dtype to int8

sd.play(audio_data, sample_rate)
sd.play(audio_data, sample_rate)

bsod = Tk()
bsod.state("zoomed")
bsod.configure(bg="#0262AF")
bsod.wm_attributes("-toolwindow", 1)

bsodfrown = Label(bsod, text=":(", bg="#0262AF", fg="white", font=("consolas", 200))
bsodfrown.pack(pady=20)

bsoddetails = Label(bsod, text="Your PC ran into a problem that it could not handle, and now it needs to restart", bg="#0262AF", fg="white", font=("classic console neue", 30), wraplength=800)
bsoddetails.pack(pady=20)

bsoddetails = Label(bsod, text="ERR_NETWORK_DISCONECCTED_SUICIDE", bg="#0262AF", fg="white", font=("classic console neue", 10), wraplength=800)
bsoddetails.pack(pady=20)

bsod.after(5000,bsod.destroy)

bsod.mainloop()



sys.exit()

