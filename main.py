from button import Button
from fan import Fan
from wifi import Wifi
from config import *
import socket

def dbg(msg):
    print("Info: " + msg)

# Connect Wifi
wifi = Wifi()
wifi.connect(SSID, PWD)

# Init Button
btn = Button(BTN_PIN, BTN_IDLE)

# Init Fan
fan = Fan(FAN_PIN, FAN_DEFAULT_FREQ, FAN_DEFAULT_DUTY)

# Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(5)

while True:
    cl, addr = s.accept()
    cl_file = cl.makefile('rwb', 0)
    
    try:
        (method, url, version) = cl_file.readline().split(b" ")
    except:
        url = '/'
    if 'poweron' in url:
        btn.short_press()
    elif 'poweroff' in url:
        btn.long_press()
    elif 'fan' in url:
        (path, query) = url.split(b"?", 2)
        params = query.split(b'&')
        freq = int(params[0].split(b'=')[-1])
        duty = int(params[1].split(b'=')[-1])
        fan.update(freq, duty)
    else:
        pass

    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    response = HTML % (fan.freq, fan.duty)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()


