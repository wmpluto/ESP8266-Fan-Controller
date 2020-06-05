import network

class Wifi():
    def __init__(self):
        self.sta_if = network.WLAN(network.STA_IF)
    
    def connect(self, ssid, pwd):
        if not self.sta_if.isconnected():
            self.sta_if.active(True)
            self.sta_if.connect(ssid, pwd)
            while not self.sta_if.isconnected():
                pass
    
    def info(self):
        return self.sta_if.ifconfig()

def main():
    from config import *
    w = Wifi()
    w.connect(SSID, PWD)
    print(w.info())

if __name__ == "__main__":
    main()