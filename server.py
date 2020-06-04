import machine
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width" />
  <title>控制界面</title>
  <style>
    .board button {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      border: 4px solid white;
      margin: 1px;
    }
  </style>
</head>

<body>
  <table class="board">
    <tr><td><a>开关机</a></td></tr>
    <tr>
      <td><button type="button" style="background-color:green" onclick="window.location.href = '/poweron?'">开机</button></td>
      <td></td>
      <td><button type="button" style="background-color:red" onclick="window.location.href = '/poweroff?'">关机</button></td>
    </tr>
    <tr><td><a>风扇</a></td></tr>
    <tr>
      <td><a>当前状态: </a></td>
      <td><a>频率: 1 Hz</a></td>
      <td><a>占空比: 1024/1024</a></td>
    </tr>
    <tr><td><a>更新参数: </a></td></tr>
  </table>
  <form action="/fan">
    频率: <input type="text" name="freq">
    <br>占空: <input type="text" name="duty">
    <br><br><input type="submit" value="设置">
  </form> 
</body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(5)

print('listening on', addr)
from machine import Pin, PWM

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    (method, url, version) = cl_file.readline().split(b" ")
    print(url)
    if 'poweron' in url:
        p0 = Pin(2, Pin.OUT)
        p0.on() 
    elif 'poweroff' in url:
        p0 = Pin(2, Pin.OUT)
        p0.off()
    elif 'fan' in url:
        pwm = PWM(Pin(0), freq=20000, duty=512)
    else:
        pass

    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html #% '\n'.join(rows)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()