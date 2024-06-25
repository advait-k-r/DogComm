import urllib.request
import keyboard
import time

while True:
    if keyboard.is_pressed("b"):
        try:
            webUrl = urllib.request.urlopen("https://n41jqjz7a5.execute-api.us-west-2.amazonaws.com/Send/dogbutton")
        except:
            pass
        time.sleep(1)
    else:
        pass
