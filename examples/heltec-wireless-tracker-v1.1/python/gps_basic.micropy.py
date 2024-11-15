from machine import Pin, UART

# Turn on voltage for GNSS
vgnss = Pin(3, Pin.OUT)
vgnss.value(1)

uart1= UART(1)
uart1.init(baudrate=115200, bits=8, parity=None, stop=1, tx=Pin(34), rx=Pin(33), timeout=300)

while True:
    # Message overview: https://receiverhelp.trimble.com/alloy-gnss/en-us/NMEA-0183messages_MessageOverview.html
    # or https://aprs.gids.nl/nmea/#gsa
    # 
    # In particular, GSV format: https://receiverhelp.trimble.com/alloy-gnss/en-us/NMEA-0183messages_GSV.html
    # $GPGSV indicates GPS and SBAS satellites. If the PRN is greater than 32, this indicates an SBAS PRN, 87 should be added to the GSV PRN number to determine the SBAS PRN number.
    # $GLGSV indicates GLONASS satellites. 64 should be subtracted from the GSV PRN number to determine the GLONASS PRN number.
    # $GBGSV indicates BeiDou satellites. 100 should be subtracted from the GSV PRN number to determine the BeiDou PRN number.
    # $GAGSV indicates Galileo satellites.
    # $GQGSV indicates QZSS satellites.
    gps_sentence = uart1.readline()
    print (gps_sentence)
   