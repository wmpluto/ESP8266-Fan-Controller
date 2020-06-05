import time
from machine import Pin, PWM

# fan can be enabled on all pins except Pin(16)
class Fan():
    def __init__(self, pin_num, freq, duty):
        self.fan = PWM(Pin(pin_num))
        self.freq = freq
        self.duty = duty
    
    def start(self):
        self.fan.freq(self.freq)
        self.fan.duty(self.duty)

    def stop(self):
        self.fan.deinit()
    
    def update(self, freq, duty):
        self.freq = freq
        self.duty = duty
        self.start()

def main():
    import time
    print("test fan @ IO0")
    f = Fan(0, 100, 512)
    f.start()
    time.sleep(1)
    f.update(10, 100)
    time.sleep(1)
    f.stop()

if __name__ == "__main__":
    main()
