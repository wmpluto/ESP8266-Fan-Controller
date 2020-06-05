import _thread, time
from machine import Pin

class Button():
    def __init__(self, pin_num, idle_status):
        self.pin = Pin(pin_num, Pin.OUT)
        self.idle_status = 1 if idle_status else 0
        self.active_status = 0 if idle_status else 1

    def set_pulse(self, t):
        self.pin.value(self.active_status)
        time.sleep(t)
        self.pin.value(self.idle_status)

    def short_press(self):
        _thread.start_new_thread(self.set_pulse, (1, ))

    def long_press(self):
        _thread.start_new_thread(self.set_pulse, (10, ))

def main():
    b = Button(2, 0)
    b.long_press()
    
if __name__ == "__main__":
    main()
    