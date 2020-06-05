# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import wifi
wifi.main()
import webrepl
webrepl.start()

