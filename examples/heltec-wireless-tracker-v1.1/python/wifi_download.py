# Scan available networks and connect to one of them.
# Then download a sample document.

import network
import socket

# set interface in station mode.
station_if = network.WLAN(network.STA_IF)
# activate the interface
station_if.active(True)
# scan and report found 2.4ghz networks
station_if.scan()
station_if.connect("<ssid>", "<passwd>")

# Try and download
# http://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf

server_addr = socket.getaddrinfo("www.espressif.com", 80)[0][-1]
s = socket.socket()
s.connect(server_addr)

_, _, host, path = "http://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf".split('/', 3)
s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))

with open("esp32-s3_datasheet_en.pdf", "wb") as f:
  while True:
    data = s.recv(100)
    if data:
      f.write(data)
    else:
      break
s.close()

print("Downloaded file to esp32-s3_datasheet_en.pdf")
