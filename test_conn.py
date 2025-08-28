import network

ssid = 'MicroPython-AP'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)
