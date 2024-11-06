import wifi
monitor = wifi.Monitor(channel=1, queue=128)
while True:
    packet = monitor.packet()
    if packet != {}:
        print(packet)