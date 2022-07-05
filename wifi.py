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
