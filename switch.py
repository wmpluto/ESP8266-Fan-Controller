import time
from machine import Pin

LOW = 0
HIGH = 1
class Switch():
    def __init__(self, pin_num, default_status):
        self.pin = Pin(pin_num, Pin.OUT)
        if default_status:
            self.set_high()
        else:
            self.set_low()
    
    def set_pulse(self):
        self.set_low()
        time.sleep(1)
        self.set_high()
    
    def set_low(self):
        self.status = LOW
        self.pin.value(LOW)
    
    def set_high(self):
        self.status = HIGH
        self.pin.value(HIGH)

def main():
    print('test switch @ IO0')
    s = Switch(0, HIGH)
    s.set_pulse()

if __name__ == "__main__":
    main()
