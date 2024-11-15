# Scan available networks and connect to one of them.

import network

# set interface in station mode.
station_if = network.WLAN(network.STA_IF)

# activate the interface
station_if.active(True)

# scan and report found 2.4ghz networks
station_if.scan()

# connect to a network
station_if.connect("<ssid>", "<passwd>")

# get the interface's MAC address
station_if.config('mac')

# get the interface's IP address
station_if.ipconfig('addr4')