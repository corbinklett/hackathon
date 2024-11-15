import network

ap = network.WLAN(network.AP_IF) 
ap.active(True) 

# Auth modes for AP mode
# 0 – open
# 1 – WEP
# 2 – WPA-PSK
# 3 – WPA2-PSK
# 4 – WPA/WPA2-PSK

ap.config(essid="test-eps32")
ap.config(authmode=3, password="foopassword1")
