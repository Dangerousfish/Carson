from lcd1602 import LCD1602 # LED Library
from machine import ADC, I2C, Pin # PICO Library
from utime import sleep # Time library
import network
import secrets

#Define Vars
LED = Pin(16,Pin.OUT) # Set LED to be D16
LIGHT_INPUT = ADC(1) # Set light sensor to ADC1

# Enable Display
i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=40000) # Set I2C params
d = LCD1602(i2c, 2, 16) # DataType, No. Lines, Chars/line
d.display() # Turn on Display
d.clear
sleep(1)

# Join Wifi using secrets.py
max_wait = 10
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

wifistatus = wlan.status()
status = wlan.ifconfig()

while max_wait > 0:
    if wifistatus < 3 or wifistatus > 3:
        break
    max_wait -= 1
    d.setCursor(0, 0)
    d.print("connecting..")
    sleep(1)
    d.clear()

    if wifistatus == 3:
        d.setCursor(0, 0)
        d.clear
        d.print("Wi-Fi Enabled!")
        d.setCursor(0, 1)
        d.print("IP: ")
        d.setCursor(4,1)
        d.print(status[0]) # IP Address

while True:
    sleep(3)
    d.clear()
    inVal = (LIGHT_INPUT.read_u16())
    d.setCursor(2, 0)
    d.print("Light Value")
    d.setCursor(5, 1)
    d.print(str(inVal))
    sleep(1)
            
    if inVal > 1000 and inVal < 99999:
        LED.value(1)
        sleep(1)
        d.clear()
        d.setCursor(0, 0)
        d.print ('The box is:')
        d.setCursor(5, 1)
        d.print('-OPEN-')
        sleep(3)
    else:
        LED.value(0)
        sleep(1)
        d.clear()
        d.setCursor(0, 0)
        d.print ('The box is:')
        d.setCursor(5,1)
        d.print('-CLOSED-')
        sleep(3)
