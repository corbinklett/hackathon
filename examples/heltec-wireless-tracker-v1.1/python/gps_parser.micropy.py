from machine import Pin, UART
from micropyGPS import MicropyGPS

# Turn on voltage for GNSS
vgnss = Pin(3, Pin.OUT)
vgnss.value(1)

uart1= UART(1)
uart1.init(baudrate=115200, bits=8, invert=0, parity=None, stop=1, tx=Pin(34), rx=Pin(33), timeout=10000)

micropy_gps = MicropyGPS()
micropy_gps.start_logging('gps_data.txt')

i = 0
max = 10000
while i < max:
    # Message overview: https://receiverhelp.trimble.com/alloy-gnss/en-us/NMEA-0183messages_MessageOverview.html
    # or https://aprs.gids.nl/nmea/#gsa
    # 
    # In particular, GSV format: https://receiverhelp.trimble.com/alloy-gnss/en-us/NMEA-0183messages_GSV.html
    # $GPGSV indicates GPS and SBAS satellites. If the PRN is greater than 32, this indicates an SBAS PRN, 87 should be added to the GSV PRN number to determine the SBAS PRN number.
    # $GLGSV indicates GLONASS satellites. 64 should be subtracted from the GSV PRN number to determine the GLONASS PRN number.
    # $GBGSV indicates BeiDou satellites. 100 should be subtracted from the GSV PRN number to determine the BeiDou PRN number.
    # $GAGSV indicates Galileo satellites.
    # $GQGSV indicates QZSS satellites.
    gps_sentence_bytes = uart1.readline()
    micropy_gps.write_log("\n")
    i = i + 1
    
    if gps_sentence_bytes is not None:
        # Convert bytes into string and remove newline and carriage return
        gps_sentence = gps_sentence_bytes.decode("ascii").strip()
        print("")
        print(gps_sentence)
        for ch in gps_sentence:
            micropy_gps.update(ch)
   
        print(f'Latitude:{micropy_gps.latitude_string()}, longitude:{micropy_gps.longitude_string()}')
        print(f'Satellite: in_use: {micropy_gps.satellites_in_use}, used:{micropy_gps.satellites_used}')
        print(f'Satellite: visible: {micropy_gps.satellites_visible()}')
        
micropy_gps.stop_logging()